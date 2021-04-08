from .model_helpers import model_runner
from io import BytesIO
from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename

bp = Blueprint('gesture_recognition_bp', __name__, template_folder='templates')

@bp.route('/api/projects/gesture_recognition', methods=['GET'])
def api_route():
    return jsonify({'status': 'in_progress'})

@bp.route('/projects/gesture_recognition', methods=['GET', 'POST'])
def app_route():
    if request.method == 'POST':
        f = request.files['formFile']

        print(type(f.read()))
        # f.save(secure_filename(f.filename))
        print(type(f.read()))
        output = model_runner.run(f.read())
        print(f, output)
        return render_template('gesture_recognition.html')
        #return render_template('gesture_recognition.html', data={'input': f, 'output': output})
    else:
        return render_template('gesture_recognition.html')