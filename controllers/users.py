from flask import Blueprint, request, jsonify
from models.user import User, UserSchema

user_schema = UserSchema()
api = Blueprint('users', __name__)

@api.route('/users/<int:user_id>', methods=['GET'])
def show(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user), 200
