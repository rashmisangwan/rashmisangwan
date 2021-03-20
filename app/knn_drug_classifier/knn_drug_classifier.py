from .model_helpers import model_runner
from flask import Blueprint, render_template
from flask import render_template, request, jsonify

bp = Blueprint('knn_drug_classifier_bp', __name__, template_folder='templates')

@bp.route('/api/projects/basic_project', methods=['GET'])
def api_route():
    data = request.args.to_dict()
    output = model_runner.run(data)

    return jsonify({
        'input': {
            'age': data['age'], 
            'gender': data['gender'], 
            "bp": data['bp'], 
            "cholestrol": data['cholesterol'], 
            "na_to_k": data['na_to_k']
        },
        'output': {
            "drug_suggested": str(output)
        }
    })


@bp.route('/projects/basic_project', methods=['GET', "POST"])
def app_route():
    if request.method == 'POST':
        data = request.form.to_dict()
        output = model_runner.run(data)

        return render_template('knn_drug_classifier.html', data={'input': data, 'output': output})
    else:
        return render_template('knn_drug_classifier.html')
