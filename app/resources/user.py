from flask import Blueprint, request, jsonify
from app.extensions import db
from app.schemas import user_schema, users_schema
from app.models import User


user_bp = Blueprint('users', __name__)


@user_bp.route('/', methods=['GET'])
def get_users():
    '''
        Queries all users
    '''
    users = User.query.all()
    return users_schema.jsonify(users)


@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id: int):
    '''
        Queries a user by id
    '''
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)


@user_bp.route('/add', methods=['POST'])
def add_user():
    '''
        Posts a new user
    '''
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data provided!'})
    
    user = user_schema.load(data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201


@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id: int):
    '''
        Updates a user by id
    '''
    user = User.query.get_or_404(id)
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data provided!'}), 400
    
    updated_user = user_schema.load(data, instance=user, partial=True)
    db.session.commit()
    return user_schema.jsonify(updated_user)


@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    '''
        Deletes a user by id 
    '''
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully!'}), 200

