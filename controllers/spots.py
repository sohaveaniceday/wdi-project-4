from flask import Blueprint, request, jsonify
from models.spot import Spot, SpotSchema, Comment, CommentSchema

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
def create():
    spot, errors = spot_schema.load(request.get_json())
    if errors:
        return jsonify(errors, 422)
    spot.save()
    return spot_schema.jsonify(spot)

@api.route('/spots/<int:spot_id>', methods=['PUT'])
def update(spot_id):
    spot = Spot.query.get(spot_id)
    spot, errors = spot_schema.load(request.get_json(), instance=spot, partial=True)
    if errors:
        return jsonify(errors, 422)
    spot.save()
    return spot_schema.jsonify(spot)

@api.route('/spots/<int:spot_id>', methods=['DELETE'])
def delete(spot_id):
    spot = Spot.query.get(spot_id)
    spot.remove()
    return '', 204

# Coming soon
# @api.route('/spots/<int:spot_id>/comments', methods=['POST'])
# def createcomment(spot_id):
#     spot = Spot.query.get(spot_id)
#     comment, errors = comment_schema.load(request.get_json())
#     if errors:
#         return jsonify(errors, 422)
#     comment.save()
#     return comment_schema.jsonify(comment)
