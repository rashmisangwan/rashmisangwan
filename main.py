import os
from app import create_app, socketio

def create_app():
    _app = create_app()
    _app.config['UPLOAD_FOLDER'] = 'uploads'
    
    port = int(os.environ.get('PORT', 8080))
    #_app.run(host = "0.0.0.0", port = port, debug = True)
    socketio.run(_app, host= "0.0.0.0", port = port, debug = True)

if __name__ == '__main__':
    create_app()
