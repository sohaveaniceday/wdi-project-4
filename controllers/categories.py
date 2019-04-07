from flask import Blueprint, request, jsonify
from models.category import Category, CategorySchema
from app import db

api = Blueprint('categories', __name__)

category_schema = CategorySchema(many=True)


@api.route('/categories', methods=['GET'])
def index():
    categories = Category.query.all()

    return category_schema.jsonify(categories, many=True), 200

@api.route('/categories/<int:category_id>', methods=['GET'])
def show(category_id):
    category = Category.query.get(category_id)
    return category_schema.jsonify(category), 200

@api.route('/categories', methods=['POST'])
def create():
    category, errors = category_schema.load(request.get_json())
    if errors:
        return jsonify(errors, 422)
    category.save()
    return category_schema.jsonify(category)

@api.route('/categories/<int:category_id>', methods=['PUT'])
def update(category_id):
    category = Category.query.get(category_id)
    category, errors = category_schema.load(request.get_json(), instance=category, partial=True)
    if errors:
        return jsonify(errors, 422)
    category.save()
    return category_schema.jsonify(category)

@api.route('/categories/<int:category_id>', methods=['DELETE'])
def delete(category_id):
    category = Category.query.get(category_id)
    category.remove()
    return '', 204
