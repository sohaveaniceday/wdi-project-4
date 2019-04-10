from app import db, ma
from marshmallow import fields
from .base import BaseModel

class Artist(db.Model, BaseModel):

    __tablename__ = 'artists'

    name = db.Column(db.String(40), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(200), nullable=False)

class ArtistSchema(ma.ModelSchema):

    spots = fields.Nested(
    'SpotSchema', many=True,
    exclude=('artists', 'comments', 'categories', 'user')
    )


    class Meta:
        model = Artist
