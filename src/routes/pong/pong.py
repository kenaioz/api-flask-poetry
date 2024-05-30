from flask import Blueprint, jsonify
from services.pong.pong import PongService

ping = Blueprint('pong', __name__)
pong_service = PongService()

@ping.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(pong_service.get_pong())