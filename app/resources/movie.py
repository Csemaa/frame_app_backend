from flask import Blueprint, request, jsonify
from app.models import Movie
from app.schemas import movie_schema, movies_schema
from app.extensions import db
from flask import send_file

movie_bp = Blueprint('movies', import_name=__name__)


@movie_bp.route('/', methods=['GET'])
def get_movies():
    '''
        Queries all movies
    '''
    movies = Movie.query.all()
    return movies_schema.jsonify(movies)


@movie_bp.route('/<int:id>', methods=['GET'])
def get_movie(id: int):
    '''
        Queries a movie by id
    '''
    movie = Movie.query.get_or_404(id)
    return movie_schema.jsonify(movie)


@movie_bp.route('/add', methods=['POST'])
def add_movie():
    '''
        Posts a new movie
    '''
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data provided!'}), 400
    
    movie = movie_schema.load(data)
    db.session.add(movie)
    db.session.commit()
    return movie_schema.jsonify(movie), 201


@movie_bp.route('/<int:id>', methods=['PUT'])
def update_movie(id: int):
    '''
        Updates a movie by id
    '''
    movie = Movie.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data provided!'})
    
    updated_movie = movie_schema.load(data, instance=movie, partial=True)
    db.session.commit()

    return movie_schema.jsonify(updated_movie)


@movie_bp.route('/<int:id>', methods=['DELETE'])
def delete_movie(id: int):
    '''
        Deletes a movie by id
    '''
    movie = Movie.query.get_or_404(id)

    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully!'}), 200


@movie_bp.route('/<int:id>/stream', methods=['GET'])
def stream_movie(id: int):
    '''
    Streams a movie file by movie ID
    '''
    movie = Movie.query.get_or_404(id)

    return send_file(
        movie.path,
        mimetype=movie.mimetype or 'video/mp4',
        as_attachment=False
    )
