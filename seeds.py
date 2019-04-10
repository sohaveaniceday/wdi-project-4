from app import app, db
from models.spot import Spot, Comment, Image
from models.category import Category
from models.artist import Artist
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all() #drops all our tables
    db.create_all() #remake our tables

    jack, errors = user_schema.load({
        'username': 'jack',
        'email': 'jack@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.526313,
        'locationlon': -0.078687
    })

    dave, errors = user_schema.load({
        'username': 'dave',
        'email': 'dave@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.46593,
        'locationlon': -0.10652
    })

    jamie, errors = user_schema.load({
        'username': 'jamie',
        'email': 'jamie@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.54057,
        'locationlon': -0.14334
    })

    if errors:
        raise Exception(errors)

    db.session.add(jack)
    db.session.add(dave)
    db.session.add(jamie)

    banksy = Artist(
    name='Banksy',
    image='https://media.wmagazine.com/photos/594d6daa0870db45df5a5d9a/4:3/w_1536/GettyImages-501590118.jpg',
    bio='Banksy is an anonymous England-based street artist, vandal, political activist, and film director.'
    )
    unknown = Artist(
    name='unknown',
    image='https://www.evolvefish.com/thumbnail.asp?file=assets/images/vinyl%20decals/EF-VDC-00035(black).jpg&maxx=300&maxy=0',
    bio='??'
    )
    kingrobbo = Artist(
    name='King Robbo',
    image='https://www.evolvefish.com/thumbnail.asp?file=assets/images/vinyl%20decals/EF-VDC-00035(black).jpg&maxx=300&maxy=0',
    bio='An English underground graffiti artist. His feud with the artist Banksy was the subject of a Channel 4 television documentary called Graffiti Wars.'
    )
    jamescochran = Artist(
    name='James Cochran',
    image='https://s3-ap-southeast-2.amazonaws.com/www.yooyahcloud.com/JIMMYC/EVRJec/Me_with_wall_for_web2.jpg',
    bio='James Cochran, also known as Jimmy C, is an English-born Australian artist best known for his urban narrative paintings and for his drip painting style.'
    )

    skating = Category(name='skating')
    graphic = Category(name='graphic')
    political = Category(name='political')
    professional = Category(name='space')
    feud = Category(name='feud')
    funny = Category(name='funny')
    tribute = Category(name='tribute')
    music = Category(name='music')

    banksyspot = Spot(
    name='Banksy\'s \'Designated Graffiti Area\'',
    locationlat=51.526313,
    locationlon=-0.078687,
    categories=[political, professional],
    artists=[banksy],
    creator=jack
    )
    graffititunnel = Spot(
    name='The Graffiti Tunnel',
    locationlat=51.501938,
    locationlon=-0.115688,
    categories=[graphic, skating, professional],
    artists=[unknown],
    creator=jack
    )
    banksyvskingrobbo = Spot(
    name='Banksy versus King Robbo',
    locationlat=51.54105512601242,
    locationlon=-0.1400870559515965,
    categories=[feud, funny],
    artists=[banksy,kingrobbo],
    creator=dave
    )
    davidbowiemural = Spot(
    name='David Bowie Mural',
    locationlat=51.4629565033388,
    locationlon=-0.115363618748619,
    categories=[tribute, music, professional],
    artists=[jamescochran],
    creator=dave
    )

    comment1 = Comment(content='I love this place', spot=banksyspot, creator=jack)
    comment2 = Comment(content='So so cool', spot=graffititunnel, creator=jack)

    image1 = Image(path='https://lh5.googleusercontent.com/p/AF1QipMtzak-8tSN965UrRkbbw2ZvPYA_5njAmSCX6vZ=w203-h152-k-no', spot=banksyspot, creator=jack)
    image2 = Image(path='https://lh5.googleusercontent.com/p/AF1QipPTFVahZU8IKx47m-XxgV0h5sY7HDS4Vbb9lfm1=s1031-k-no', spot=graffititunnel, creator=jack)
    image3 = Image(path='https://lh5.googleusercontent.com/p/AF1QipNnZUE8vreCSKA1U_E61Qhu5NFl85WLjezbuYH_=s1031-k-no', spot=graffititunnel, creator=jack)
    image4 = Image(path='https://assets.londonist.com/uploads/2017/06/i875/4222541880_4b92f0a45e_b.jpg', spot=banksyvskingrobbo, creator=dave)
    image5 = Image(path='https://media.timeout.com/images/103024083/image.jpg', spot=davidbowiemural, creator=dave)

    db.session.add(banksy)
    db.session.add(unknown)
    db.session.add(kingrobbo)
    db.session.add(jamescochran)

    db.session.add(skating)
    db.session.add(graphic)
    db.session.add(political)
    db.session.add(professional)
    db.session.add(feud)
    db.session.add(funny)
    db.session.add(tribute)
    db.session.add(music)

    db.session.add(banksyspot)
    db.session.add(graffititunnel)
    db.session.add(banksyvskingrobbo)
    db.session.add(davidbowiemural)
    db.session.add(comment1)
    db.session.add(comment2)

    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)

    db.session.commit()
