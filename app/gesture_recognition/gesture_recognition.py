from .model_helpers import model_runner
from io import BytesIO
import os
import base64
from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
from flask_socketio import emit, join_room, leave_room

from .. import socketio

bp = Blueprint('gesture_recognition_bp', __name__, template_folder='templates')

@bp.route('/api/projects/gesture_recognition', methods=['GET'])
def api_route():
    f = request.files['formFile']
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    f.save(file_path)

    output = model_runner.run(file_path)
    f.seek(0)

    encoded = base64.b64encode(f.read()).decode()
    return jsonify(
        {'input': 'data:image/png;base64,{}'.format(encoded), 'output': output})


@bp.route('/projects/gesture_recognition', methods=['GET', 'POST'])
def app_route():
    if request.method == 'POST':
        f = request.files['formFile']

        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        
        f.save(file_path)
        
        output = model_runner.run(file_path)
        
        f.seek(0)
        encoded = base64.b64encode(f.read()).decode()
        
        return render_template('gesture_recognition.html', data={'input': 'data:image/png;base64,{}'.format(encoded), 'output': output})
    else:
        return render_template('gesture_recognition.html')

from PIL import Image
from base64 import decodestring

@socketio.on('image_frame')
def image_frame(data):
    decoded = base64.b64decode(data)
    decodedBytes = BytesIO(decoded)

    im = Image.open(decodedBytes)

    im.save('image.png', 'PNG')
    output = model_runner.run('image.png')
    emit('response_back', str(output[0]))  ## ??
