from flask import Blueprint, request, jsonify
from models.artist import Artist, ArtistSchema
from app import db

api = Blueprint('artists', __name__)

artist_schema = ArtistSchema(many=True)

@api.route('/artists', methods=['GET'])
def index():
    artists = Artist.query.all()

    return artist_schema.jsonify(artists, many=True), 200

@api.route('/artists/<int:artist_id>', methods=['GET'])
def show(artist_id):
    artist = Artist.query.get(artist_id)
    return artist_schema.jsonify(artist), 200

@api.route('/artists', methods=['POST'])
def create():
    artist, errors = artist_schema.load(request.get_json())
    if errors:
        return jsonify(errors, 422)
    artist.save()
    return artist_schema.jsonify(artist)

@api.route('/artists/<int:artist_id>', methods=['PUT'])
def update(artist_id):
    artist = Artist.query.get(artist_id)
    artist, errors = artist_schema.load(request.get_json(), instance=artist, partial=True)
    if errors:
        return jsonify(errors, 422)
    artist.save()
    return artist_schema.jsonify(artist)

@api.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete(artist_id):
    artist = Artist.query.get(artist_id)
    artist.remove()
    return '', 204
