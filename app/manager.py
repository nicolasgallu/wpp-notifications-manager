from flask import Blueprint, request, request, jsonify
from app.logger import logger
from app.pipeline import send_rquest
import threading

wpp_bp = Blueprint("wpp_manager", __name__, url_prefix="/webhook/messages")
@wpp_bp.route('', methods=['POST'])
def handle_webhook(): 
    payload = request.json
    try:
        message = payload['messages'][0]['text']['body']
        if "bot no pudo responder" in message and "<su respuesta aquí>" not in message:
            thread = threading.Thread(target=send_rquest, args=([message]))
            thread.start()
            return jsonify({"status": "success", "message": "Callback received"}), 200
        else:
            return jsonify({"status": "success", "message": "Callback received"}), 200
    except:
        return jsonify({"status": "success", "message": "Callback received"}), 200