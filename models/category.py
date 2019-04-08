from app import db, ma
from marshmallow import fields
from .base import BaseModel

class Category(db.Model, BaseModel):

    __tablename__ = 'categories'

    name = db.Column(db.String(40), unique=True, nullable=False)

class CategorySchema(ma.ModelSchema):

    spots = fields.Nested(
    'SpotSchema', many=True,
    exclude=('categories', 'comments', 'creator', 'artists')
    )

    class Meta:
        model = Category
