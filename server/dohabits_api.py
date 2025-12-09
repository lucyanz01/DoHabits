from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Objetivo, Tarea
from services import (
    crear_usuario,
    obtener_usuario,
    crear_objetivo,
    obtener_objetivos,
    crear_tarea,
    obtener_tareas
)
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def home():
    return "API funcionando"

# Usuarios 

@app.route("/usuarios", methods = ["POST"])
def api_crear_usuario():
    data = request.get_json()
    respuesta, status = crear_usuario(
        session,
        data.get("username"),
        data.get("password")
        )
    return jsonify(respuesta), status

@app.route("/usuarios/<int:usuario_id>", methods=["GET"])
def api_obtener_usuario(usuario_id):
    respuesta, status = obtener_usuario(session, usuario_id)
    return jsonify(respuesta), status

# Objetivos 

@app.route("/objetivos", methods=["POST"])
def api_crear_objetivo():
    data = request.get_json()
    respuesta, status = crear_objetivo(
        session,
        data.get("usuario_id"),   # obligatorio
        data.get("titulo")
    )
    return jsonify(respuesta), status

@app.route("/objetivos/<int:usuario_id>", methods=["GET"])
def api_obtener_objetivos(usuario_id):
    respuesta, status = obtener_objetivos(session, usuario_id)
    return jsonify(respuesta), status

# Tareas

@app.route("/tareas", methods=["POST"])
def api_crear_tarea():
    data = request.get_json()
    respuesta, status = crear_tarea(
        session,
        data.get("objetivo_id"),
        data.get("descripcion") # nombre
    )
    return jsonify(respuesta), status


@app.route("/tareas/<int:objetivo_id>", methods=["GET"])
def api_obtener_tareas(objetivo_id):
    respuesta, status = obtener_tareas(session, objetivo_id)
    return jsonify(respuesta), status

if __name__ == "__main__":
    app.run(debug=True)
