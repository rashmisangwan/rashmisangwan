from flask import Flask

from flask_socketio import SocketIO, emit

socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .home import home
        from .knn_drug_classifier import knn_drug_classifier
        from .gesture_recognition import gesture_recognition
        
        app.register_blueprint(home.bp)
        app.register_blueprint(knn_drug_classifier.bp)
        app.register_blueprint(gesture_recognition.bp)

        socketio.init_app(app)

        return app
