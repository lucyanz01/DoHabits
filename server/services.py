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

