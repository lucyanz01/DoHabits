import jwt 
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from flask import jsonify, request, Blueprint, current_app
from functools import wraps
from config import session
from models import Usuario
from backend.utils.security import verify_password
from backend.services.usuarios import crear_usuario

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no definida")

bp = Blueprint("auth", __name__)

def crear_token(usuario_id):
    payload = {
        "sub": usuario_id,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=24)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error":"token requerido"}), 401

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )
            request.user_id = payload["sub"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error":"token inválido"}), 401
        
        return f(*args, **kwargs)
    return decorated

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "cuerpo de solicitud vacio"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password: 
        return jsonify({"error": "datos faltantes"}), 400
        
    usuario = session.query(Usuario).filter_by(username=username).first()

    if not usuario or not verify_password(password, usuario.password):
        return jsonify({"error": "credenciales inválidas"}), 401
    
    token = crear_token(usuario.id)
    return jsonify({"token": token}), 200

@bp.route("/usuarios", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "cuerpo de solicitud vacio"}), 400
    
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "datos faltantes"})
    
    resultado, status = crear_usuario(session, username, password)

    return jsonify(resultado), status