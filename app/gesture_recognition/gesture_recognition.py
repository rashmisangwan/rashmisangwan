from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('gesture_recognition_bp', __name__, template_folder='templates')


@bp.route('/api/projects/gesture_recognition', methods=['GET'])
def gesture_handler():
    
    return "hello..welcome back"