from flask import Flask, request, jsonify, render_template
from dohabits import Usuario, Objetivo, Tarea

app = Flask(__name__)

usuarios = {} # Diccionario global de usuarios

@app.route("/")
def home():
    return render_template("")

@app.route("/usuarios/iniciar", methods=["POST"])
def iniciar_usuario():
    data = request.json
    nombre = data["nombre"]

    if nombre not in usuarios:
        usuarios[nombre] = Usuario(nombre)

    return jsonify({"mensaje": f"Usuario {nombre} iniciado"})