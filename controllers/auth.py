from flask import Blueprint, jsonify, request
from models.user import User, UserSchema
from lib.helpers import is_unique


api = Blueprint('auth', __name__)
user_schema = UserSchema()

@api.route('/register', methods=['POST'])
def register():
    user, errors = user_schema.load(request.get_json())

    if errors:
        return jsonify(errors), 422

    user.save()

    return jsonify({'message': 'Registration Successful'}), 201
