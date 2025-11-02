import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_cannot_be_read'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://movies.ssqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    HOST = '127.0.0.1'
    PORT = 5000


class DevelopmentConfig(Config):
    HOST = '127.0.0.1'


class ProductiontConfig(Config):
    HOST = '0.0.0.0'