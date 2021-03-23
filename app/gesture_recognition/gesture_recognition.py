from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('gesture_recognition_bp', __name__, template_folder='templates')


@bp.route('/api/projects/gesture_recognition', methods=['GET'])
def api_route():
    return jsonify({'status': 'in_progress'})

@bp.route('/projects/gesture_recognition', methods=['GET'])
def app_route():
    return "status :: in progress"