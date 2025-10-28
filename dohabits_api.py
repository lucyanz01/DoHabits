from flask import Flask, request, jsonify, render_template
from dohabits import Usuario, Objetivo, Tarea

app = Flask(__name__)

nombres_user = {} # Diccionario global de usuarios

@app.route("/")
def home():
    return jsonify({"mensaje": "API activa"})

@app.route("/usuario", methods=["POST"])
def crear_usuario():
    data = request.json
    nombre = data["nombre"]

    if nombre not in nombres_user:
        nombres_user[nombre] = Usuario(nombre)

    return jsonify({"mensaje": f"Usuario {nombre} iniciado"})

@app.route("/usuarios/<nombre>/objetivos", methods=["POST"])
def crear_objetivos(nombre):
    data = request.json
    nombre_obj = data["nombre_obj"]

    if nombre in nombres_user:
        nombres_user[nombre].crear_objetivo(nombre_obj)
        return jsonify({"mensaje": f"Objetivo: '{nombre_obj}' creado."})
    return jsonify ({"error": "usuario no existe"}), 404