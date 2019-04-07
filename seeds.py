from app import app, db
from models.spot import Spot, Comment
from models.category import Category
from models.artist import Artist
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all() #drops all our tables
    db.create_all() #remake our tables

    jack, errors = user_schema.load({
        'username': 'beanslord',
        'email': 'jack@email.com',
        'password': 'password',
        'password_confirmation': 'password',
        'locationlat': 51.526313,
        'locationlon': -0.078687
    })

    if errors:
        raise Exception(errors)


    db.session.add(jack)

    banksy = Artist(
    name='Banksy',
    image='https://media.wmagazine.com/photos/594d6daa0870db45df5a5d9a/4:3/w_1536/GettyImages-501590118.jpg',
    bio='Banksy is an anonymous England-based street artist, vandal, political activist, and film director.'
    )

    skating = Category(name='skating')
    graphic = Category(name='graphic')
    political = Category(name='political')
    professional = Category(name='space')

    banksyspot = Spot(
    name='Banksy\'s \'Designated Graffiti Area\'',
    locationlat=51.526313,
    locationlon=-0.078687,
    categories=[political, professional],
    artists=[banksy],
    user=jack
    )
    graffititunnel = Spot(
    name='The Graffiti Tunnel',
    locationlat=51.501938,
    locationlon=-0.115688,
    categories=[graphic, skating],
    user=jack
    )

    comment1 = Comment(content='I love this place', spot=banksyspot)
    comment2 = Comment(content='This place sucks', spot=graffititunnel)

    db.session.add(banksy)

    db.session.add(skating)
    db.session.add(graphic)
    db.session.add(political)
    db.session.add(professional)

    db.session.add(banksyspot)
    db.session.add(graffititunnel)
    db.session.add(comment1)
    db.session.add(comment2)

    db.session.commit()
