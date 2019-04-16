from app import db, ma
from marshmallow import fields
from .base import BaseModel
from .category import Category, CategorySchema
from .artist import Artist, ArtistSchema
from .user import User, UserSchema

likes = db.Table(
    'likes',
    db.Column('spot_id', db.Integer, db.ForeignKey('spots.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

categories_spots = db.Table('categories_spots',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    db.Column('spot_id', db.Integer, db.ForeignKey('spots.id'), primary_key=True)
)

artists_spots = db.Table('artists_spots',
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
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
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_spots')
    liked_by = db.relationship('User', secondary=likes, backref='likes')


class SpotSchema(ma.ModelSchema):
    comments = fields.Nested(
    'CommentSchema', many=True,
    only=('content', 'id', 'created_at', 'creator')
    )
    images = fields.Nested('ImageSchema', many=True, only=('path', 'id', 'creator'))
    categories = fields.Nested('CategorySchema', many=True, only=('name', 'id'))
    artists = fields.Nested('ArtistSchema', many=True, only=('name', 'id', 'bio', 'image', 'spots'))
    creator = fields.Nested("UserSchema", only=('id', 'username'))
    liked_by = fields.Nested('UserSchema', many=True, only=('id', 'username'))

    class Meta:
        model = Spot

class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'))
    spot = db.relationship('Spot', backref='comments')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_comments')

class CommentSchema(ma.ModelSchema):
    creator = fields.Nested("UserSchema", only=('id', 'username'))


    class Meta:
        model = Comment

class Image(db.Model, BaseModel):

    __tablename__ = 'images'

    path = db.Column(db.Text, nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'))
    spot = db.relationship('Spot', backref='images')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_images')


class ImageSchema(ma.ModelSchema):
    creator = fields.Nested("UserSchema", only=('id', 'username'))

    class Meta:
        model = Image
