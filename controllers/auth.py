from flask import Blueprint, jsonify, request
from models.user import User, UserSchema
from lib.helpers import is_unique

api = Blueprint('auth', __name__)
user_schema = UserSchema()

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    user, errors = user_schema.load(request.get_json())

    if not is_unique(model=User, key='username', value=data['username']):
        errors['username'] = errors.get('username', []) + ['Username already taken']

    if not is_unique(model=User, key='email', value=data['email']):
        errors['email'] = errors.get('email', []) + ['Email already taken']

    if errors:
        return jsonify(errors), 422

    user.save()

    return jsonify({'message': 'Registration Successful'}), 201
