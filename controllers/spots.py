from flask import Blueprint, request, jsonify, g
from models.spot import Spot, SpotSchema, Comment, CommentSchema, ImageSchema, Image
from lib.secure_route import secure_route
from models.category import Category
from models.artist import Artist


spot_schema = SpotSchema()
comment_schema = CommentSchema()
image_schema = ImageSchema()
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
    categories = list(data['category_id'])
    artists = list(data['artist_id'])
    categories_models = []
    artists_models = []
    for x in categories:
        categories_models.append(Category.query.get(x))
    for x in artists:
        artists_models.append(Artist.query.get(x))
    spot.creator = g.current_user
    for x in categories_models:
        spot.categories.append(x)
    for x in artists_models:
        spot.artists.append(x)
    spot.save()
    return spot_schema.jsonify(spot)

@api.route('/spots/<int:spot_id>', methods=['PUT'])
@secure_route
def update(spot_id):
    data = request.get_json()
    spot = Spot.query.get(spot_id)
    spot, errors = spot_schema.load(request.get_json(), instance=spot, partial=True)
    if errors:
        return jsonify(errors), 422
    if spot.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    category = Category.query.get(data['category_id'])
    spot.categories.append(category)
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

@api.route('/spots/<int:spot_id>/images', methods=['POST'])
@secure_route
def image_create(spot_id):
    data = request.get_json()
    spot = Spot.query.get(spot_id)
    image, errors = image_schema.load(request.get_json(data))
    if errors:
        return jsonify(errors), 422
    image.spot = spot
    image.creator = g.current_user
    image.save()
    return image_schema.jsonify(image)

@api.route('/spots/<int:spot_id>/images/<int:image_id>', methods=['DELETE'])
@secure_route
def image_delete(**kwargs):
    image = Image.query.get(kwargs['image_id'])
    if image.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    image.remove()
    return '', 204

@api.route('/spots/<int:spot_id>/like', methods=['PUT'])
@secure_route
def like(spot_id):
    spot = Spot.query.get(spot_id)
    user = g.current_user
    spot.liked_by.append(user)
    spot.save()
    return spot_schema.jsonify(spot), 200
