from app import app, db

from models.spot import Spot

with app.app_context():
    db.drop_all() #drops all our tables
    db.create_all() #remake our tables

    banksy = Spot(
    name='Banksy\'s \'Designated Graffiti Area\'',
    locationlat=51.526313,
    locationlon=-0.078687
    )
    graffititunnel = Spot(
    name='The Graffiti Tunnel',
    locationlat=51.501938,
    locationlon=-0.115688
    )

    # add the planets to the session
    db.session.add(banksy)
    db.session.add(graffititunnel)

    # commit that data to the database
    db.session.commit()
