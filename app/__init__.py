from flask import Flask
from config import DevelopmentConfig
from app.extensions import db, ma

def create_app():
    # Create app obj and config
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Init extensions
    db.init_app(app)
    ma.init_app(app)

    return app
