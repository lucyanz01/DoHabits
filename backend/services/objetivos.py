from models import Objetivo
from sqlalchemy.orm import Session

def crear_objetivo(session:Session, usuario_id:int, titulo:str):
    existe = session.query(Objetivo).filter_by(usuario_id=usuario_id, titulo=titulo).first()
    if existe:
        return {"error": "El objetivo ya existe"}, 400

    nuevo_objetivo = Objetivo(titulo=titulo, usuario_id=usuario_id)
    session.add(nuevo_objetivo)
    session.commit()
    return {"mensaje": "Objetivo creado con éxito", "id": nuevo_objetivo.id}, 201

def obtener_objetivos(session:Session, usuario_id:int):
    objetivos = session.query(Objetivo).filter_by(usuario_id=usuario_id).all()
    if not objetivos:
        return {"error": "No hay objetivos creados"}, 404
    
    resultado = []
    for obj in objetivos:
        resultado.append({
            "id": obj.id,
            "titulo": obj.titulo,
            "progreso": obj.progreso()
        })

    return {"objetivos": resultado}, 200