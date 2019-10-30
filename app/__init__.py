from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config_options


db = SQLAlchemy()
login_manager = LoginManager()

bootstrap = Bootstrap()
mail = Mail()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message_category = 'info'


def create_app(Config_name):

    
    app = Flask(__name__)
    app.config.from_object(config_options[Config_name])
    login_manager.init_app(app)
    db.init_app(app)
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app
