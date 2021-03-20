from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .home import home
        from .knn_drug_classifier import knn_drug_classifier 
        
        app.register_blueprint(home.bp)
        app.register_blueprint(knn_drug_classifier.bp)

        return app
