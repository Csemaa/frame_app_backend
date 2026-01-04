from flask import Blueprint, jsonify, request
from app.extensions import db
from app.schemas import usertag_schema, usertags_schema, movies_schema
from app.models import UserTag, Movie


usertag_bp = Blueprint('user_tag', __name__)

usertag_options= ['favourite', 'watch_later']

@usertag_bp.route('/', methods=['GET'])
def get_all_tags():
    '''
        Returns a list of tags that by the user

        user_id: int - The id of the user
    '''
    
    usertags = UserTag.query.all()

    return usertags_schema.jsonify(usertags)


@usertag_bp.route('/<int:user_id>', methods=['GET'])
def get_tags(user_id: int):
    '''
        Returns a list of tags that by the user

        user_id: int - The id of the user
    '''
    
    if user_id is None:
        return jsonify({'error': 'Parameter user_id is missing from the body!'}), 400
    
    filtered_usertags = UserTag.query.filter_by(user_id=user_id).all()

    return usertags_schema.jsonify(filtered_usertags)


@usertag_bp.route('/<int:user_id>/movies', methods=['GET'])
def get_tagged_movies(user_id: int):
    '''
        Returns a list of movies that the user tagged

        user_id: int - The id of the user
    '''
    
    if user_id is None:
        return jsonify({'error': 'Parameter user_id is missing from the body!'}), 400
    
    filtered_usertags = UserTag.query.filter_by(user_id=user_id).all()
    movie_ids = [usertag.movie_id for usertag in filtered_usertags]
    movies = Movie.query.filter(Movie.id.in_(movie_ids)).all()

    return movies_schema.jsonify(movies)


@usertag_bp.route('/', methods=['POST'])
def tag_movie():
    '''
        Adds a tag to a movie with the user_id
    '''
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data provided!'}), 400
    

    if data.get('tag') is None or data.get('tag') not in usertag_options:
        return jsonify({'error': 'Invalid tag provided!'}), 400
    

    new_usertag = usertag_schema.load(data)
    db.session.add(new_usertag)
    db.session.commit()

    return usertag_schema.jsonify(new_usertag), 201


@usertag_bp.route('/<int:id>', methods=['DELETE'])
def remove_tag(id: int):
    '''
        Deletes a tag
    '''
    user_tag = UserTag.query.get_or_404(id)
    db.session.delete(user_tag)
    db.session.commit()
    return jsonify({'message': 'Usertag deleted successfully!'}), 200