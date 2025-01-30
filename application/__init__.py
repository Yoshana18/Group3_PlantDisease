from flask import Flask
from application.config import Config
from application.auth import auth

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(auth)

    return app
