from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .model import UserModel


login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    # crear instancia flask
    app = Flask(__name__)
    app.config.update(DEBUG=True, ENV='development')
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app 