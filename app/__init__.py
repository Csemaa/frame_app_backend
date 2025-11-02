from flask import Flask
from config import DevelopmentConfig
from app.extensions import db, ma
from app.resources.movie import movie_bp
from app.resources.user import user_bp
from app.resources.usertag import usertag_bp


def create_app():
    # Create app obj and config
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Init extensions
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(movie_bp, url_prefix='/api/movies')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(usertag_bp, url_prefix='/api/usertags')

    return app
