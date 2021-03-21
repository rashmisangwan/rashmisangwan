import os
from app import create_app 

if __name__ == '__main__':
    _app = create_app()
    port = int(os.environ.get('PORT', 8080))
    _app.run(host = "0.0.0.0", port = port, debug = True)
    
    