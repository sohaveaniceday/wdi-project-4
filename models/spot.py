from app import db, ma
from marshmallow import fields
from .base import BaseModel
from .category import Category, CategorySchema
from .artist import Artist, ArtistSchema
from .user import User, UserSchema

categories_spots = db.Table('categories_spots',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    db.Column('spot_id', db.Integer, db.ForeignKey('spots.id'), primary_key=True)
)

artists_spots = db.Table('artists_spots',
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
    db.Column('spot_id', db.Integer, db.ForeignKey('spots.id'), primary_key=True)
)

users_spots = db.Table('users_spots',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('spot_id', db.Integer, db.ForeignKey('spots.id'), primary_key=True)
)


class Spot(db.Model, BaseModel):

    __tablename__ = 'spots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    locationlat = db.Column(db.Float, nullable=False)
    locationlon = db.Column(db.Float, nullable=False)
    categories = db.relationship('Category',
    secondary=categories_spots, backref='spots')
    artists = db.relationship('Artist',
    secondary=artists_spots, backref='spots')
    # coming soon
    user = db.relationship('User',
    secondary=users_spots, backref='spots', uselist=False)


class SpotSchema(ma.ModelSchema):
    comments = fields.Nested('CommentSchema', many=True, only=('content', 'id', 'created_at'))
    images = fields.Nested('ImageSchema', many=True, only=('path', 'id'))
    categories = fields.Nested('CategorySchema', many=True, only=('name', 'id'))
    artists = fields.Nested('ArtistSchema', many=True, only=('name', 'id'))
    user = fields.Nested('UserSchema', only=('username', 'id'))

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

class Image(db.Model, BaseModel):

    __tablename__ = 'images'

    path = db.Column(db.Text, nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'))
    spot = db.relationship('Spot', backref='images')

class ImageSchema(ma.ModelSchema):

    class Meta:
        model = Image
