from models import Usuario, Objetivo, Tarea
from sqlalchemy.orm import Session

def crear_usuario(session: Session, username: str, password: str):
    existe = session.query(Usuario).filter_by(username = username).first()
    if existe:
        return {"error": "El usuario ya existe"}, 400
    
    usuario = Usuario(username=username, password=password)
    session.add(usuario)
    session.commit()
    return {"mensaje": "Usuario creado con éxito"}, 201

def obtener_usuario(session:Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return {"error": "Usuario no encontrado"},  404

def crear_objetivo(session, usuario_id, titulo):
    existe = session.query(Objetivo).filter_by(usuario_id=usuario_id, titulo=titulo).first()
    if existe:
        return {"error": "El objetivo ya existe"}, 400
    
    objetivo = Objetivo(titulo=titulo, usuario_id=usuario_id)
    session.add(objetivo)
    session.commit()
    return {"mensaje": "Objetivo creado con éxito", "id": objetivo.id}, 201

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