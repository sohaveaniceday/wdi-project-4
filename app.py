from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/spots'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# pylint: disable=C0413
from models.spot import Spot, SpotSchema

spot_schema = SpotSchema()


#index route
@app.route('/spots', methods=['GET'])
def index():
    spots = Spot.query.all()

    return spot_schema.jsonify(spots, many=True), 200

@app.route('/spots/<int:spot_id>', methods=['GET'])
def show(spot_id):
    spot = Spot.query.get(spot_id)
    return spot_schema.jsonify(spot), 200
