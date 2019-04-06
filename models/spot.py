from app import db, ma
from marshmallow import fields
from .base import BaseModel
# from .category import Category

# categories_scififilms = db.Table('categories_scififilms',
#     db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
#     db.Column('scififilm_id', db.Integer, db.ForeignKey('scififilms.id'), primary_key=True)
# )

class Spot(db.Model, BaseModel):

    __tablename__ = 'spots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    locationlat = db.Column(db.Float, nullable=False)
    locationlon = db.Column(db.Float, nullable=False)
    # artist = db.Column(db.String(40), nullable=False)
    # categories = db.relationship('Category',
    # secondary=categories_scififilms, backref='scififilms')

class SpotSchema(ma.ModelSchema):
    comments = fields.Nested('SpotSchema', many=True, exclude=('spot',))
    # categories = fields.Nested('CategorySchema', many=True)
    class Meta:
        model = Spot

class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'))
    spot = db.relationship('Spot', backref='comments')

class CommentSchema(ma.ModelSchema):

    class Meta:
        model = Comment
