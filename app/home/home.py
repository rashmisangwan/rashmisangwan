from flask import Blueprint, render_template

bp = Blueprint(
    'home_bp', __name__, template_folder='templates'
)

@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')
