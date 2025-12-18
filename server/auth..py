import jwt 
import os
from datetime import datetime, timedelta, timezone
from flask import jsonify, request, Blueprint, current_app
from functools import wraps

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