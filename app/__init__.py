from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

def create_app():
    # crear instancia flask
    app = Flask(__name__)
    app.config.update(DEBUG=True, ENV='development')
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)
    app.register_blueprint(auth)

    return app 