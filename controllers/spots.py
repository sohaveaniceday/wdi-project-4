from flask import Blueprint, request, jsonify, g
from models.spot import Spot, SpotSchema, Comment, CommentSchema
from lib.secure_route import secure_route
from models.category import Category



spot_schema = SpotSchema()
comment_schema = CommentSchema()
api = Blueprint('spots', __name__)

@api.route('/spots', methods=['GET'])
def index():
    spots = Spot.query.all()

    return spot_schema.jsonify(spots, many=True), 200

@api.route('/spots/<int:spot_id>', methods=['GET'])
def show(spot_id):
    spot = Spot.query.get(spot_id)
    return spot_schema.jsonify(spot), 200

@api.route('/spots', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    spot, errors = spot_schema.load(data)
    if errors:
        return jsonify(errors), 422
    category = Category.query.get(data['category_id'])
    spot.creator = g.current_user
    spot.categories.append(category)
    spot.save()
    return spot_schema.jsonify(spot)

@api.route('/spots/<int:spot_id>', methods=['PUT'])
@secure_route
def update(spot_id):
    spot = Spot.query.get(spot_id)
    spot, errors = spot_schema.load(request.get_json(), instance=spot, partial=True)
    if errors:
        return jsonify(errors), 422
    if spot.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    spot.save()
    return spot_schema.jsonify(spot)

@api.route('/spots/<int:spot_id>', methods=['DELETE'])
@secure_route
def delete(spot_id):
    spot = Spot.query.get(spot_id)
    if spot.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    spot.remove()
    return '', 204

@api.route('/spots/<int:spot_id>/comments', methods=['POST'])
@secure_route
def comment_create(spot_id):
    data = request.get_json()
    spot = Spot.query.get(spot_id)
    comment, errors = comment_schema.load(request.get_json(data))
    if errors:
        return jsonify(errors), 422
    comment.spot = spot
    comment.creator = g.current_user
    comment.save()
    return comment_schema.jsonify(comment)

@api.route('/spots/<int:spot_id>/comments/<int:comment_id>', methods=['DELETE'])
@secure_route
def comment_delete(**kwargs):
    comment = Comment.query.get(kwargs['comment_id'])
    if comment.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    comment.remove()
    return '', 204

@api.route('/spots/<int:spot_id>/like', methods=['PUT'])
@secure_route
def like(spot_id):
    spot = Spot.query.get(spot_id)
    user = g.current_user
    spot.liked_by.append(user)
    spot.save()
    return spot_schema.jsonify(spot), 200
