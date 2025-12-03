from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Objetivo, Tarea
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def home():
    return "Funcionando"

@app.route("/usuarios", methods = ["POST"])
def crear_usuario():
    data = request.get_json()

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Faltan nombre de usuario o contraseña"}), 400
    
    nuevo_usuario = Usuario(
        username = data["username"],
        password = data["password"]
    )

    session.add(nuevo_usuario)
    session.commit()
    
    return jsonify({"mensaje": "Usuario creado", "id": nuevo_usuario.id}), 201