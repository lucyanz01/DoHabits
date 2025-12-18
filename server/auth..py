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

