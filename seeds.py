from app import app, db

from models.spot import Spot, Comment
from models.category import Category
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all() #drops all our tables
    db.create_all() #remake our tables

    jack, errors = user_schema.load({
        'username': 'beanslord',
        'email': 'jack@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)


    db.session.add(jack)



    skating = Category(name='skating')
    graphic = Category(name='graphic')
    political = Category(name='political')
    professional = Category(name='space')

    banksy = Spot(
    name='Banksy\'s \'Designated Graffiti Area\'',
    locationlat=51.526313,
    locationlon=-0.078687,
    categories=[political, professional]
    )
    graffititunnel = Spot(
    name='The Graffiti Tunnel',
    locationlat=51.501938,
    locationlon=-0.115688,
    categories=[graphic, skating]
    )

    comment1 = Comment(content='I love this place', spot=banksy)
    comment2 = Comment(content='This place sucks', spot=graffititunnel)

    db.session.add(skating)
    db.session.add(graphic)
    db.session.add(political)
    db.session.add(professional)
    # add the planets to the session
    db.session.add(banksy)
    db.session.add(graffititunnel)
    db.session.add(comment1)
    db.session.add(comment2)

    # commit that data to the database
    db.session.commit()
