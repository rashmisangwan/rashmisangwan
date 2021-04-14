import os
from app import create_app, socketio

server_app = create_app()
server_app.config['UPLOAD_FOLDER'] = 'uploads'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    socketio.run(server_app, host = "0.0.0.0", port = 8080, debug = True)
