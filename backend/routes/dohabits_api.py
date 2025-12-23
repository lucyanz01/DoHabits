from flask import Blueprint, request, jsonify
from config import session
from models import Tarea, Objetivo
from backend.routes.auth import token_required
from backend.services.objetivos import crear_objetivo, obtener_objetivos
from backend.services.tareas import crear_tarea, obtener_tareas

bp_api = Blueprint("api", __name__)

@bp_api.route("/objetivos", methods=["GET", "POST"])
@token_required
def manejar_objetivos():
    user_id = request.user_id
    if request.method == "GET":
        resultado, status = obtener_objetivos(session, user_id)
        return jsonify(resultado), status

    data = request.get_json()
    resultado, status = crear_objetivo(session, user_id, data.get("titulo"))
    return jsonify(resultado), status

@bp_api.route("/objetivos/<int:obj_id>/tareas", methods=["GET", "POST"])
@token_required
def manejar_tareas(obj_id):
    user_id = request.user_id
    if request.method == "GET":
        resultado, status = obtener_tareas(session, user_id, obj_id)
        return jsonify(resultado), status

    data = request.get_json()
    resultado, status = crear_tarea(session, data.get("descripcion"), user_id, obj_id)
    return jsonify(resultado), status

@bp_api.route("/tareas/<int:tarea_id>/completar", methods=["PATCH"])
@token_required
def tarea_completada(tarea_id):
    user_id = request.user_id
    
    tarea = session.query(Tarea).join(Objetivo).filter(
        Tarea.id == tarea_id,
        Objetivo.usuario_id == user_id
    ).first()

    if not tarea:
        return jsonify({"error": "No encontrada"}), 404
    
    tarea.marcar_completada()
    session.commit()

    return jsonify({"mensaje": f"Tarea '{tarea.descripcion}' marcada como completada"}), 200

@bp_api.route("/tareas/<int:tarea_id>/desmarcar", methods=["PATCH"])
@token_required
def desmarcar(tarea_id):
    user_id = request.user_id

    tarea = session.query(Tarea).join(Objetivo).filter(
        Tarea.id == tarea_id, 
        Objetivo.usuario_id == user_id
    ).first()

    if not tarea:
        return jsonify({"error": "No encontrada"}), 404
    
    tarea.desmarcar_completada()
    session.commit()

    return jsonify({"mensaje": "Tarea desmarcada"}), 200