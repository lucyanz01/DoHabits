from models import Tarea, Objetivo
from sqlalchemy.orm import Session

def crear_tarea(session:Session, descripcion:str, usuario_id:int, objetivo_id:int):
    objetivo = session.query(Objetivo).filter_by(id=objetivo_id, usuario_id=usuario_id).first()

    if not objetivo:
        return {"error": "Acceso denegado"}, 403
    
    existe = session.query(Tarea).filter_by(objetivo_id=objetivo_id, descripcion=descripcion).first()
    if existe:
        return {"error": "La tarea ya existe"}, 400
    
    nueva_tarea = Tarea(descripcion=descripcion, objetivo_id=objetivo_id)
    session.add(nueva_tarea)
    session.commit()
    return {"mensaje": "Tarea creada con éxito", "id": nueva_tarea.id}, 201

def obtener_tareas(session: Session, usuario_id: int, objetivo_id: int):
    objetivo = session.query(Objetivo).filter_by(id=objetivo_id, usuario_id=usuario_id).first()
    
    if not objetivo:
        return {"error": "Acceso denegado"}, 403
    
    tareas = session.query(Tarea).filter_by(objetivo_id=objetivo_id).all()
    if not tareas:
        return {"error": "No hay tareas creadas"}, 404
    
    resultado = []
    for t in tareas:
        resultado.append({
            "id": t.id,
            "descripcion": t.descripcion,
            "completada": t.completada
        })

    return {"tareas": resultado}, 200