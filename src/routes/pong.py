from flask import Blueprint, jsonify
from services.pong import PongService

ping = Blueprint("ping", __name__)
pong_service = PongService()


@ping.route("/ping", methods=["GET"])
def ping_pong():
    print("pong")
    return jsonify(pong_service.get_pong())
