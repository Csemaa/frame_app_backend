from app import db
from datetime import datetime


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    imdb_id = db.Column(db.String(128))
    path = db.Column(db.String(512))
    last_time_viewed = db.Column(db.DateTime, nullable=True, default=datetime.now())

    tags = db.relationship('UserTag', back_populates='movie', cascade='all, delete-orphan')


class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(128))
    nickname = db.Column(db.String(32))
    profile_picture = db.Column(db.String(64))

    tags = db.relationship('UserTag', back_populates='user', cascade='all, delete-orphan')


class UserTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.ForeignKey('movie.id'), nullable=False)
    tag = db.Column(db.String(128)) # For storing watch later, and favourite values

    user = db.relationship('User', back_populates='tags')
    movie = db.relationship('Movie', back_populates='tags')

    

