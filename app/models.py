from app import db
from datetime import datetime


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    imdb_id = db.Column(db.String(128))
    path = db.Column(db.String(512))
    last_time_viewed = db.Column(db.Datetime(), nullable=True, default=datetime.now().isoformat())


class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(128))
    nickname = db.Column(db.String(32))
    profile_picture = db.Column(db.String(32))


class UserTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    tag = db.Column(db.String(128)) # For store watch later, and favourite values

    

