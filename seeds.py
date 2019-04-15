from app import app, db
from models.spot import Spot, Comment, Image
from models.category import Category
from models.artist import Artist
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all() #drops all our tables
    db.create_all() #remake our tables

    sarah, errors = user_schema.load({
        'username': 'sarah',
        'email': 'sarah@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.496645,
        'locationlon': -0.117358
    })
    nehal, errors = user_schema.load({
        'username': 'nehal',
        'email': 'nehal@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.458636,
        'locationlon': -0.067885
    })
    joelle, errors = user_schema.load({
        'username': 'joelle',
        'email': 'joelle@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.493227,
        'locationlon': -0.157588
    })
    robyn, errors = user_schema.load({
        'username': 'robyn',
        'email': 'robyn@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.453180,
        'locationlon': -0.189357
    })
    dave, errors = user_schema.load({
        'username': 'dave',
        'email': 'dave@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.523930,
        'locationlon': -0.062996
    })
    ollie, errors = user_schema.load({
        'username': 'ollie',
        'email': 'ollie@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.455416,
        'locationlon': -0.026508
    })
    paul, errors = user_schema.load({
        'username': 'paul',
        'email': 'paul@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.518125,
        'locationlon': -0.114529
    })
    jamie, errors = user_schema.load({
        'username': 'jamie',
        'email': 'jamie@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.480067,
        'locationlon': -0.118980
    })
    phil, errors = user_schema.load({
        'username': 'phil',
        'email': 'phil@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.534658,
        'locationlon': -0.203813
    })
    hannah, errors = user_schema.load({
        'username': 'hannah',
        'email': 'hannah@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.502639,
        'locationlon': -0.194697
    })
    jacob, errors = user_schema.load({
        'username': 'jacob',
        'email': 'jacob@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.516738,
        'locationlon': -0.112476
    })
    emily, errors = user_schema.load({
        'username': 'emily',
        'email': 'emily@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.549827,
        'locationlon': -0.094059
    })
    sandra, errors = user_schema.load({
        'username': 'sandra',
        'email': 'sandra@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.535928,
        'locationlon': -0.260063
    })
    john, errors = user_schema.load({
        'username': 'john',
        'email': 'john@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.545090,
        'locationlon': -0.212095
    })
    adam, errors = user_schema.load({
        'username': 'adam',
        'email': 'adam@email',
        'password': 'pass',
        'password_confirmation': 'pass',
        'locationlat': 51.474513,
        'locationlon': -0.238726
    })

    if errors:
        raise Exception(errors)

    db.session.add(sarah)
    db.session.add(nehal)
    db.session.add(joelle)
    db.session.add(robyn)
    db.session.add(dave)
    db.session.add(ollie)
    db.session.add(paul)
    db.session.add(jamie)
    db.session.add(phil)
    db.session.add(hannah)
    db.session.add(jacob)
    db.session.add(emily)
    db.session.add(sandra)
    db.session.add(john)
    db.session.add(adam)

    unknown = Artist(
    name='Unknown',
    image='http://catchingfire.ca/wp-content/uploads/2016/09/question-mark-square-01.png',
    bio='??'
    )
    adamneate = Artist(
    name='Adam Neate',
    image='https://payload.cargocollective.com/1/19/631832/10501211/12039259_873405492712656_50445661618073459_n-2_960.jpg',
    bio='Adam Neate (born 1977) is a British painter, conceptual artist and described by The Telegraph in 2008 as one of the world\'s best-known street artists.'
    )
    alexmartinez = Artist(
    name='Alex Martinez',
    image='https://d26gcd16fgpb1d.cloudfront.net/images/moodclips/2015/7/26/59551/68ab0c340c7f2416559cb1c21ad7e5a3-g4i.jpg',
    bio='Alex Martinez (also known by his Tag name SHINE) is a United States-born international artist who specialises in graffiti art.'
    )
    andycouncil = Artist(
    name='Andy Council',
    image='https://farm9.staticflickr.com/8468/28669393686_8715641167_b.jpg',
    bio='Andy Council is an illustrator and graffiti artist from Bristol, UK. Dinosaurs combined with architecture are a common theme of his designs.'
    )
    banksy = Artist(
    name='Banksy',
    image='https://pixel.nymag.com/imgs/daily/vulture/2017/06/23/23-banksy.w330.h330.jpg',
    bio='Banksy is an anonymous England-based street artist, vandal, political activist, and film director.'
    )
    beneine = Artist(
    name='Beneine',
    image='https://www.artrepublic.com/media/catalog/product/cache/1/small_image/280x/9df78eab33525d08d6e5fb8d27136e95/b/e/beneine.jpg',
    bio='Ben Flynn (born 23 August 1970), known professionally as Eine, is an English street artist based in London.'
    )
    cartrain = Artist(
    name='Cartrain',
    image='https://imitatemodern.com/wp-content/uploads/2016/12/Chered-1000x1000.jpg',
    bio='Cartrain (born 1991), often stylised cartяain, is a British artist associated with the graffiti urban art movement.'
    )
    christiaannagel = Artist(
    name='Christiaan Nagel',
    image='http://www.about-street-art.com/wp-content/uploads/2017/04/CHRISTIAAN-NAGEL-LONDON-Great-Eastern-Street-Photo2017-03-07-Street-Art-mushrom.jpg',
    bio='Christiaan Nagel is a British street artist known for his oversized mushroom sculptures made from polyurethane.'
    )
    cutup = Artist(
    name='Cutup',
    image='http://www.jaguarshoes.com/wp-content/uploads/2011/03/Cut-Up_Machine_15-300x300.jpg',
    bio='Cutup is a group of London-based artists, whose work mainly revolves around the manipulation of billboard advertisements.'
    )
    darrencullen = Artist(
    name='Darren Cullen',
    image='https://is2-ssl.mzstatic.com/image/thumb/Purple118/v4/eb/6d/32/eb6d324e-f459-9471-0c76-1952c3497802/source/256x256bb.jpg',
    bio='Darren Cullen is a London-based professional graffiti artist who is commonly known by the tag name SER. '
    )
    guydenning = Artist(
    name='Guy Denning',
    image='https://i.pinimg.com/originals/fe/85/60/fe8560e8cd88dc2755b46345d93efcd5.jpg',
    bio='Guy Denning (born 1965) is a self taught English contemporary artist and painter based in France. '
    )
    inkie = Artist(
    name='Inkie',
    image='https://www.upfest.co.uk/files/cache/500x500_1145_41e22dc8e606653d2bfb18efaac18d03',
    bio='Inkie is a London-based painter and street artist, originally from Clifton, Bristol'
    )
    jamescochran = Artist(
    name='James Cochran',
    image='https://i.pinimg.com/originals/07/81/d3/0781d3dcb0b41f02f43563b2f4c48ff6.jpg',
    bio='James Cochran, also known as Jimmy C, is an English-born Australian artist best known for his urban narrative paintings and for his drip painting style.'
    )
    kingrobbo = Artist(
    name='King Robbo',
    image='https://www.blouinartinfo.com/sites/default/files/styles/970w576h/public/migrated/6/272063%3AKing_Robbo_0.jpg?itok=GX4OhcYx',
    bio='An English underground graffiti artist. His feud with the artist Banksy was the subject of a Channel 4 television documentary called Graffiti Wars.'
    )
    nickwalker = Artist(
    name='Nickwalker',
    image='https://www.nellyduff.com/wp-content/uploads/2018/12/artist-thumbnail-Nick_Walker.jpg',
    bio='Nick Walker (born 1969) is a graffiti artist originating from Bristol, England. His paintings often feature a bowler-hatted gentleman \'vandal\'.'
    )
    paulinsect = Artist(
    name='Paul Insect',
    image='https://www.artcollectorz.com/assets/managed/images/cache/ABLUQAAADUA2AAIAAAAAAHIBDUA7777774AAAAAATMAVQAQA.jpg',
    bio='Paul Insect is a UK contemporary artist, who is most famous for his 2007 solo show Bullion exhibition at London\'s Art gallery, Lazarides Gallery.'
    )
    phlegm = Artist(
    name='Phlegm',
    image='https://i.pinimg.com/originals/c7/00/f7/c700f7ed553ae781edc858cd82b76412.jpg',
    bio='Phlegm is a Welsh-born Sheffield-based muralist and artist who first developed his illustrations in self-published comics.'
    )
    richsimmons = Artist(
    name='Rich Simmons',
    image='https://imitatemodern.com/wp-content/uploads/2016/10/reflections-silk-screen-blue.-rich-simmonsjpg-1000x1000.jpg',
    bio='Rich Simmons is a British pop artist based in London.'
    )
    robertdelnaja = Artist(
    name='Robert Del Naja',
    image='https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/VF_AA_PACKSHOT.jpg/220px-VF_AA_PACKSHOT.jpg',
    bio='Robert Del Naja (/dɛl ˈnaɪə/; born 21 January 1965), also known as 3D, is a British artist, musician, singer and songwriter. '
    )
    sickboy = Artist(
    name='Sickboy',
    image='https://www.artcollectorz.com/assets/managed/images/cache/ABZUAAAADUAZEAIAAAAAAHIBDUA7777774AAAAAAVEAVQAQA.jpg',
    bio='Sickboy is the name of a street artist from Bristol, UK, known for his temple logo and his \'Save the Youth\' slogan.'
    )
    stik = Artist(
    name='Stik',
    image='https://pbs.twimg.com/profile_images/723474072521285632/LSS6jHx1_400x400.jpg',
    bio='Stik is a British graffiti artist based in London. He is known for painting large stick figures.'
    )
    temper = Artist(
    name='Temper',
    image='http://img.chelmerfineart.com/original/graffiti-is-physical-18472.jpg',
    bio='Temper is an English graffiti artist. He is most prolific in the advancement of spray paint photorealism in the United Kingdom.'
    )

    db.session.add(unknown)
    db.session.add(adamneate)
    db.session.add(alexmartinez)
    db.session.add(andycouncil)
    db.session.add(banksy)
    db.session.add(beneine)
    db.session.add(cartrain)
    db.session.add(christiaannagel)
    db.session.add(cutup)
    db.session.add(darrencullen)
    db.session.add(guydenning)
    db.session.add(inkie)
    db.session.add(jamescochran)
    db.session.add(kingrobbo)
    db.session.add(nickwalker)
    db.session.add(paulinsect)
    db.session.add(phlegm)
    db.session.add(richsimmons)
    db.session.add(robertdelnaja)
    db.session.add(sickboy)
    db.session.add(stik)
    db.session.add(temper)


    threed = Category(name='3D')
    seventies = Category(name='70s')
    eighties = Category(name='80s')
    nineties = Category(name='90s')
    naughties = Category(name='00s')
    abstract = Category(name='Abstract')
    agnomical = Category(name='Agnomical')
    amorous = Category(name='Amorous')
    animal = Category(name='Animal')
    beautiful = Category(name='Beautiful')
    blockbuster = Category(name='Blockbuster')
    brick = Category(name='Brick')
    cartoon = Category(name='Cartoon')
    cool = Category(name='Cool')
    crazy = Category(name='Crazy')
    cultural = Category(name='Cultural')
    famous = Category(name='Famous')
    fatcap = Category(name='Fatcap')
    feud = Category(name='Feud')
    funny = Category(name='Funny')
    graphic = Category(name='Graphic')
    happy = Category(name='Happy')
    heaven = Category(name='Heaven')
    hiphop = Category(name='Hiphop')
    human = Category(name='Human')
    intellectual = Category(name='Intellectual')
    landmark = Category(name='Landmark')
    meta = Category(name='Meta')
    movies = Category(name='Movies')
    music = Category(name='Music')
    nature = Category(name='Nature')
    nudity = Category(name='Nudity')
    obscene = Category(name='Obscene')
    photoreal = Category(name='Photoreal')
    piece = Category(name='Piece')
    plant = Category(name='Plant')
    political = Category(name='Political')
    portrait = Category(name='Portrait')
    poster = Category(name='Poster')
    professional = Category(name='Professional')
    rooftop = Category(name='Rooftop')
    sad = Category(name='Sad')
    sex = Category(name='Sex')
    skating = Category(name='Skating')
    space = Category(name='Space')
    stencil = Category(name='Stencil')
    sticker = Category(name='Sticker')
    surreal = Category(name='Surreal')
    tag = Category(name='Tag')
    throwup = Category(name='Throw-Up')
    tribute = Category(name='Tribute')
    tv = Category(name='TV')
    videogames = Category(name='Video Games')
    violent = Category(name='Violent')
    wildstyle = Category(name='Wildstyle')

    db.session.add(threed)
    db.session.add(seventies)
    db.session.add(eighties)
    db.session.add(nineties)
    db.session.add(naughties)
    db.session.add(abstract)
    db.session.add(agnomical)
    db.session.add(amorous)
    db.session.add(animal)
    db.session.add(beautiful)
    db.session.add(blockbuster)
    db.session.add(brick)
    db.session.add(cartoon)
    db.session.add(cool)
    db.session.add(crazy)
    db.session.add(cultural)
    db.session.add(famous)
    db.session.add(fatcap)
    db.session.add(feud)
    db.session.add(funny)
    db.session.add(graphic)
    db.session.add(happy)
    db.session.add(heaven)
    db.session.add(hiphop)
    db.session.add(human)
    db.session.add(intellectual)
    db.session.add(landmark)
    db.session.add(meta)
    db.session.add(movies)
    db.session.add(music)
    db.session.add(nature)
    db.session.add(nudity)
    db.session.add(obscene)
    db.session.add(photoreal)
    db.session.add(piece)
    db.session.add(plant)
    db.session.add(political)
    db.session.add(portrait)
    db.session.add(poster)
    db.session.add(professional)
    db.session.add(rooftop)
    db.session.add(sad)
    db.session.add(sex)
    db.session.add(skating)
    db.session.add(space)
    db.session.add(stencil)
    db.session.add(sticker)
    db.session.add(surreal)
    db.session.add(tag)
    db.session.add(throwup)
    db.session.add(tribute)
    db.session.add(tv)
    db.session.add(videogames)
    db.session.add(violent)
    db.session.add(wildstyle)

    upyours = Spot(
    name='Up Yours',
    locationlat=51.466845,
    locationlon=-0.188757,
    categories=[naughties, abstract, meta],
    artists=[guydenning],
    creator=phil
    )
    swanstreet = Spot(
    name='Swan Street',
    locationlat=51.518292,
    locationlon=-0.112412,
    categories=[tag, feud, happy],
    artists=[andycouncil],
    creator=hannah
    )
    bees = Spot(
    name='Bees',
    locationlat=51.476717,
    locationlon=-0.217444,
    categories=[poster, cool, videogames],
    artists=[adamneate],
    creator=paul
    )
    squirrelnest = Spot(
    name='Squirrel Nest',
    locationlat=51.453790,
    locationlon=-0.097663,
    categories=[stencil, tv, intellectual],
    artists=[cutup],
    creator=phil
    )
    fridaforever = Spot(
    name='Frida Forever',
    locationlat=51.485781,
    locationlon=-0.219765,
    categories=[threed, plant, blockbuster],
    artists=[alexmartinez],
    creator=john
    )
    lovewilltearusapart = Spot(
    name='Love Will Tear Us Apart',
    locationlat=51.507592,
    locationlon=-0.174337,
    categories=[stencil, cartoon],
    artists=[adamneate],
    creator=dave
    )
    robopolice = Spot(
    name='Robo Police',
    locationlat=51.537965,
    locationlon=-0.210994,
    categories=[eighties, animal, space],
    artists=[andycouncil],
    creator=john
    )
    snailart = Spot(
    name='Snail Art',
    locationlat=51.455421,
    locationlon=-0.257123,
    categories=[poster, plant, crazy],
    artists=[beneine],
    creator=ollie
    )
    tunnelart = Spot(
    name='Tunnel Art',
    locationlat=51.489043,
    locationlon=-0.249404,
    categories=[brick, famous, nature],
    artists=[kingrobbo],
    creator=adam
    )
    funnybones = Spot(
    name='Funny Bones',
    locationlat=51.467248,
    locationlon=-0.213651,
    categories=[funny, human, crazy],
    artists=[kingrobbo],
    creator=adam
    )
    foxy = Spot(
    name='Foxy',
    locationlat=51.488180,
    locationlon=-0.042715,
    categories=[landmark, crazy, cartoon],
    artists=[banksy],
    creator=sarah
    )
    stickpeople = Spot(
    name='Stick People',
    locationlat=51.504182,
    locationlon=-0.189898,
    categories=[beautiful, political, funny],
    artists=[jamescochran],
    creator=dave
    )
    animalcult = Spot(
    name='Animal Cult',
    locationlat=51.495967,
    locationlon=-0.009631,
    categories=[abstract, seventies, happy],
    artists=[adamneate],
    creator=emily
    )
    ninja = Spot(
    name='Ninja',
    locationlat=51.543756,
    locationlon=-0.075633,
    categories=[sex, photoreal, obscene],
    artists=[beneine],
    creator=john
    )
    lovewall = Spot(
    name='Love Wall',
    locationlat=51.493145,
    locationlon=-0.241723,
    categories=[agnomical, violent],
    artists=[banksy],
    creator=nehal
    )
    abstractwall = Spot(
    name='Abstract Wall',
    locationlat=51.452944,
    locationlon=-0.108126,
    categories=[sex, portrait, blockbuster],
    artists=[inkie],
    creator=joelle
    )
    nervouseddy = Spot(
    name='Nervous Eddy',
    locationlat=51.489289,
    locationlon=-0.148392,
    categories=[rooftop, videogames, piece],
    artists=[inkie],
    creator=sarah
    )
    sadgirl = Spot(
    name='Sad Girl',
    locationlat=51.540311,
    locationlon=-0.218011,
    categories=[surreal, poster],
    artists=[temper],
    creator=robyn
    )
    boardart = Spot(
    name='Board Art',
    locationlat=51.465792,
    locationlon=-0.062282,
    categories=[videogames, animal, feud],
    artists=[cutup],
    creator=adam
    )
    lovelondon = Spot(
    name='Love London',
    locationlat=51.523544,
    locationlon=-0.005307,
    categories=[landmark, seventies, sex],
    artists=[kingrobbo],
    creator=phil
    )
    noescape = Spot(
    name='No Escape',
    locationlat=51.543383,
    locationlon=-0.081187,
    categories=[sad, crazy, sex],
    artists=[stik],
    creator=john
    )
    highfive = Spot(
    name='High Five',
    locationlat=51.531600,
    locationlon=-0.029347,
    categories=[amorous, sex, piece],
    artists=[richsimmons],
    creator=ollie
    )
    oldman = Spot(
    name='Old Man',
    locationlat=51.524326,
    locationlon=-0.172636,
    categories=[happy, nineties, violent],
    artists=[kingrobbo],
    creator=robyn
    )
    whiterabbit = Spot(
    name='White Rabbit',
    locationlat=51.517017,
    locationlon=-0.005231,
    categories=[hiphop, brick, cartoon],
    artists=[darrencullen],
    creator=sarah
    )
    winkwink = Spot(
    name='Wink Wink',
    locationlat=51.526437,
    locationlon=-0.070760,
    categories=[space, piece, sticker],
    artists=[banksy],
    creator=phil
    )
    hendricks = Spot(
    name='Hendricks',
    locationlat=51.466908,
    locationlon=-0.025559,
    categories=[crazy, tribute, seventies],
    artists=[sickboy],
    creator=sandra
    )
    eyeseeyou = Spot(
    name='Eye See You',
    locationlat=51.525147,
    locationlon=-0.104160,
    categories=[nudity, brick, portrait],
    artists=[robertdelnaja],
    creator=paul
    )
    colourmask = Spot(
    name='Colour Mask',
    locationlat=51.458236,
    locationlon=-0.064910,
    categories=[tribute, happy, seventies],
    artists=[richsimmons],
    creator=dave
    )
    pinkskull = Spot(
    name='Pink Skull',
    locationlat=51.489605,
    locationlon=-0.213978,
    categories=[amorous, nineties, portrait],
    artists=[inkie],
    creator=dave
    )
    turbothatcher = Spot(
    name='Turbo Thatcher',
    locationlat=51.480638,
    locationlon=-0.012324,
    categories=[graphic, obscene, happy],
    artists=[temper],
    creator=emily
    )
    bigbird = Spot(
    name='Big Bird',
    locationlat=51.506653,
    locationlon=-0.005881,
    categories=[human, tribute, amorous],
    artists=[christiaannagel],
    creator=robyn
    )
    plslike = Spot(
    name='Pls Like',
    locationlat=51.506385,
    locationlon=-0.102477,
    categories=[tag, violent, piece],
    artists=[robertdelnaja],
    creator=sarah
    )
    mananddog = Spot(
    name='Man and Dog',
    locationlat=51.539454,
    locationlon=-0.056813,
    categories=[political, skating, sticker],
    artists=[robertdelnaja],
    creator=sarah
    )
    youcompleteme = Spot(
    name='You Complete Me',
    locationlat=51.473665,
    locationlon=-0.185587,
    categories=[feud, threed, obscene],
    artists=[andycouncil],
    creator=john
    )
    destructart = Spot(
    name='Destruct Art',
    locationlat=51.534764,
    locationlon=-0.058793,
    categories=[skating, hiphop, music],
    artists=[stik],
    creator=sarah
    )
    search = Spot(
    name='Search',
    locationlat=51.546813,
    locationlon=-0.112260,
    categories=[happy, amorous, hiphop],
    artists=[beneine],
    creator=phil
    )
    gorillamask = Spot(
    name='Gorilla Mask',
    locationlat=51.507615,
    locationlon=-0.256804,
    categories=[human, piece, eighties],
    artists=[andycouncil],
    creator=sarah
    )
    thekiss = Spot(
    name='The Kiss',
    locationlat=51.484993,
    locationlon=-0.234162,
    categories=[beautiful, nineties, tribute],
    artists=[phlegm],
    creator=jacob
    )
    theaffair = Spot(
    name='The Affair',
    locationlat=51.529306,
    locationlon=-0.062691,
    categories=[animal, heaven, agnomical],
    artists=[jamescochran],
    creator=ollie
    )
    octoelephant = Spot(
    name='Octo Elephant',
    locationlat=51.529097,
    locationlon=-0.256455,
    categories=[skating, plant, animal],
    artists=[cartrain],
    creator=paul
    )
    toxic = Spot(
    name='Toxic',
    locationlat=51.549360,
    locationlon=-0.077309,
    categories=[rooftop, political, human],
    artists=[paulinsect],
    creator=john
    )
    helovesme = Spot(
    name='He Loves Me',
    locationlat=51.502438,
    locationlon=-0.137264,
    categories=[portrait, animal, music],
    artists=[richsimmons],
    creator=emily
    )
    alice = Spot(
    name='Alice',
    locationlat=51.470409,
    locationlon=-0.180681,
    categories=[tv, beautiful, nineties],
    artists=[nickwalker],
    creator=paul
    )
    coolhat = Spot(
    name='Cool Hat',
    locationlat=51.499860,
    locationlon=-0.200063,
    categories=[cool, cartoon, political],
    artists=[darrencullen],
    creator=sandra
    )
    threed = Spot(
    name='Three D',
    locationlat=51.451962,
    locationlon=-0.193132,
    categories=[photoreal, skating, nineties],
    artists=[robertdelnaja],
    creator=john
    )
    # bolt = Spot(
    # name='Bolt',
    # locationlat=51.488653,
    # locationlon=-0.076995,
    # categories=[threed, political, space],
    # artists=[jamescochran],
    # creator=phil
    # )
    truecolours = Spot(
    name='True Colours',
    locationlat=51.464895,
    locationlon=-0.000326,
    categories=[surreal, tv, crazy],
    artists=[cartrain],
    creator=phil
    )
    cartoonheaven = Spot(
    name='Cartoon Heaven',
    locationlat=51.468444,
    locationlon=-0.038840,
    categories=[amorous, music, sex],
    artists=[cutup],
    creator=emily
    )
    checkmate = Spot(
    name='Check Mate',
    locationlat=51.485773,
    locationlon=-0.164787,
    categories=[piece, plant, skating],
    artists=[christiaannagel],
    creator=ollie
    )
    thethinker = Spot(
    name='The Thinker',
    locationlat=51.508116,
    locationlon=-0.261338,
    categories=[violent, hiphop, eighties],
    artists=[adamneate],
    creator=sarah
    )
    teardownthiswall = Spot(
    name='Tear Down This Wall',
    locationlat=51.497863,
    locationlon=-0.107224,
    categories=[photoreal, plant, political],
    artists=[guydenning],
    creator=john
    )
    wackyracers = Spot(
    name='Wacky Racers',
    locationlat=51.504193,
    locationlon=-0.166645,
    categories=[eighties, amorous, portrait],
    artists=[richsimmons],
    creator=hannah
    )
    tizer = Spot(
    name='Tizer',
    locationlat=51.478742,
    locationlon=-0.145720,
    categories=[wildstyle, hiphop, cultural],
    artists=[beneine],
    creator=adam
    )
    ghostrider = Spot(
    name='Ghost Rider',
    locationlat=51.496999,
    locationlon=-0.172986,
    categories=[hiphop, seventies, famous],
    artists=[adamneate],
    creator=adam
    )
    thepowerofgirl = Spot(
    name='The Power of Girl',
    locationlat=51.514170,
    locationlon=-0.057469,
    categories=[happy, tv, hiphop],
    artists=[richsimmons],
    creator=hannah
    )
    # thethreegirls = Spot(
    # name='The Three Girls',
    # locationlat=51.500198,
    # locationlon=-0.074956,
    # categories=[sex, threed],
    # artists=[banksy],
    # creator=jamie
    # )
    skulls = Spot(
    name='Skulls',
    locationlat=51.494824,
    locationlon=-0.038125,
    categories=[professional, happy, animal],
    artists=[alexmartinez],
    creator=jamie
    )
    roar = Spot(
    name='Roar',
    locationlat=51.545241,
    locationlon=-0.043740,
    categories=[cartoon, human],
    artists=[cartrain],
    creator=paul
    )
    thecircus = Spot(
    name='The Circus',
    locationlat=51.533865,
    locationlon=-0.057309,
    categories=[photoreal, beautiful, meta],
    artists=[richsimmons],
    creator=sandra
    )
    thewolf = Spot(
    name='The Wolf',
    locationlat=51.477390,
    locationlon=-0.128618,
    categories=[amorous, fatcap, sad],
    artists=[christiaannagel],
    creator=jamie
    )
    paintwithlove = Spot(
    name='Paint With Love',
    locationlat=51.469882,
    locationlon=-0.191385,
    categories=[graphic, beautiful, cultural],
    artists=[jamescochran],
    creator=jamie
    )
    allthecolours = Spot(
    name='All the Colours',
    locationlat=51.508720,
    locationlon=-0.064281,
    categories=[stencil, blockbuster, amorous],
    artists=[beneine],
    creator=robyn
    )
    scarymary = Spot(
    name='Scary Mary',
    locationlat=51.482012,
    locationlon=-0.201759,
    categories=[poster, meta, cool],
    artists=[jamescochran],
    creator=joelle
    )
    faces = Spot(
    name='Faces',
    locationlat=51.472761,
    locationlon=-0.174415,
    categories=[blockbuster, tribute, seventies],
    artists=[banksy],
    creator=emily
    )
    trumpsays = Spot(
    name='Trump Says',
    locationlat=51.481036,
    locationlon=-0.198675,
    categories=[sad, professional, funny],
    artists=[christiaannagel],
    creator=jamie
    )
    wings = Spot(
    name='Wings',
    locationlat=51.538326,
    locationlon=-0.217142,
    categories=[music, naughties, amorous],
    artists=[stik],
    creator=robyn
    )
    cowboy = Spot(
    name='CowBoy',
    locationlat=51.547869,
    locationlon=-0.085739,
    categories=[seventies, funny, nineties],
    artists=[alexmartinez],
    creator=phil
    )
    oldlondon = Spot(
    name='Old London',
    locationlat=51.539398,
    locationlon=-0.007014,
    categories=[beautiful, tribute, movies],
    artists=[christiaannagel],
    creator=sandra
    )
    boardmeeting = Spot(
    name='Board Meeting',
    locationlat=51.523116,
    locationlon=-0.205937,
    categories=[beautiful, intellectual],
    artists=[phlegm],
    creator=robyn
    )
    timeisanillusion = Spot(
    name='Time is an Illusion',
    locationlat=51.481600,
    locationlon=-0.005741,
    categories=[nature, sticker, meta],
    artists=[christiaannagel],
    creator=emily
    )
    peace = Spot(
    name='Peace',
    locationlat=51.515280,
    locationlon=-0.018704,
    categories=[videogames, sad, rooftop],
    artists=[jamescochran],
    creator=phil
    )
    zomg = Spot(
    name='zomg',
    locationlat=51.493795,
    locationlon=-0.218063,
    categories=[nineties, brick, poster],
    artists=[stik],
    creator=phil
    )
    bull = Spot(
    name='Bull',
    locationlat=51.462520,
    locationlon=-0.172972,
    categories=[sad, photoreal, graphic],
    artists=[nickwalker],
    creator=ollie
    )
    iloveshoreditch = Spot(
    name='I Love Shoreditch',
    locationlat=51.506338,
    locationlon=-0.200131,
    categories=[fatcap, beautiful, amorous],
    artists=[darrencullen],
    creator=sarah
    )
    murdershewrote = Spot(
    name='Murder She Wrote',
    locationlat=51.464916,
    locationlon=-0.139175,
    categories=[rooftop, agnomical, obscene],
    artists=[temper],
    creator=ollie
    )
    dearsister = Spot(
    name='Dear Sister',
    locationlat=51.487968,
    locationlon=-0.137141,
    categories=[tag, beautiful, cartoon],
    artists=[unknown],
    creator=phil
    )
    coolbeans = Spot(
    name='Cool Beans',
    locationlat=51.517888,
    locationlon=-0.242311,
    categories=[animal, violent, hiphop],
    artists=[paulinsect],
    creator=paul
    )
    highnoon = Spot(
    name='High Noon',
    locationlat=51.535372,
    locationlon=-0.139364,
    categories=[feud, agnomical, happy],
    artists=[darrencullen],
    creator=hannah
    )
    snowinmay = Spot(
    name='Snow in May',
    locationlat=51.543574,
    locationlon=-0.229167,
    categories=[political, nudity, funny],
    artists=[jamescochran],
    creator=jamie
    )
    kingsguard = Spot(
    name='Kings Guard',
    locationlat=51.536578,
    locationlon=-0.011136,
    categories=[sex, human, plant],
    artists=[sickboy],
    creator=joelle
    )
    doublelove = Spot(
    name='Double Love',
    locationlat=51.504419,
    locationlon=-0.254673,
    categories=[animal, tv, photoreal],
    artists=[banksy],
    creator=emily
    )
    dontshoot = Spot(
    name='Dont Shoot',
    locationlat=51.451755,
    locationlon=-0.041901,
    categories=[cultural, happy, nineties],
    artists=[guydenning],
    creator=adam
    )
    tongueemoji = Spot(
    name='Tongue Emoji',
    locationlat=51.485281,
    locationlon=-0.015018,
    categories=[plant, rooftop, tv],
    artists=[cutup],
    creator=john
    )
    thehand = Spot(
    name='The Hand',
    locationlat=51.507587,
    locationlon=-0.041774,
    categories=[cultural, beautiful, nudity],
    artists=[inkie],
    creator=phil
    )
    londonpleasuregardens = Spot(
    name='London Pleasure Gardens',
    locationlat=51.462228,
    locationlon=-0.125557,
    categories=[violent, tag, funny],
    artists=[robertdelnaja],
    creator=sandra
    )
    ec4 = Spot(
    name='EC4',
    locationlat=51.538842,
    locationlon=-0.060175,
    categories=[music, portrait, photoreal],
    artists=[banksy],
    creator=john
    )
    entwined = Spot(
    name='Entwined',
    locationlat=51.505268,
    locationlon=-0.233023,
    categories=[famous, fatcap, abstract],
    artists=[inkie],
    creator=paul
    )
    heartandmind = Spot(
    name='Heart and Mind',
    locationlat=51.496223,
    locationlon=-0.180590,
    categories=[hiphop, landmark, naughties],
    artists=[kingrobbo],
    creator=adam
    )
    natureheart = Spot(
    name='Nature Heart',
    locationlat=51.517575,
    locationlon=-0.087477,
    categories=[famous, fatcap, abstract],
    artists=[inkie],
    creator=joelle
    )
    sunrise = Spot(
    name='Sunrise',
    locationlat=51.502373,
    locationlon=-0.069090,
    categories=[graphic, sex, intellectual],
    artists=[kingrobbo],
    creator=ollie
    )
    comingautumn = Spot(
    name='Coming Autumn',
    locationlat=51.513650,
    locationlon=-0.165127,
    categories=[happy, beautiful, nudity],
    artists=[christiaannagel],
    creator=ollie
    )
    brexitcellent = Spot(
    name='Brexitcellent',
    locationlat=51.541353,
    locationlon=-0.252474,
    categories=[space, music, piece],
    artists=[beneine],
    creator=ollie
    )
    mystic = Spot(
    name='Mystic',
    locationlat=51.488741,
    locationlon=-0.213929,
    categories=[human, political, tag],
    artists=[phlegm],
    creator=phil
    )
    lady = Spot(
    name='Lady',
    locationlat=51.522622,
    locationlon=-0.137860,
    categories=[rooftop, obscene, plant],
    artists=[adamneate],
    creator=hannah
    )
    ourheartishere = Spot(
    name='Our Heart is Here',
    locationlat=51.482520,
    locationlon=-0.162913,
    categories=[sticker, fatcap, sex],
    artists=[beneine],
    creator=phil
    )
    intergalactic = Spot(
    name='Intergalactic',
    locationlat=51.459496,
    locationlon=-0.268007,
    categories=[movies, abstract, nineties],
    artists=[stik],
    creator=emily
    )
    savebrixton = Spot(
    name='Save Brixton',
    locationlat=51.489804,
    locationlon=-0.267754,
    categories=[nineties, violent],
    artists=[darrencullen],
    creator=sandra
    )

    image1 = Image(path='https://4.bp.blogspot.com/-jtKMgo5ERz0/W3WkZlOimYI/AAAAAAAAIzE/Uwk8WHgDsIAP7yt_ha6l29iIvtNklK0ZACLcBGAs/s1600/FANAKAPAN_13_HOOKEDBLOG_PHOTO_2018_MARK_RIGNEY.jpg', spot=upyours, creator=jacob)
    image2 = Image(path='http://emilyluxton.co.uk/wp-content/uploads/2015/04/wpid-img_20150410_181625-600x600.jpg', spot=swanstreet, creator=nehal)
    image3 = Image(path='https://www.thisiscolossal.com/wp-content/uploads/2015/03/bees-2.jpg', spot=bees, creator=ollie)
    image4 = Image(path='https://i.pinimg.com/736x/0d/54/da/0d54da799177b730a6dcb8cdc29da7ea--smiley-faces-futurism.jpg', spot=squirrelnest, creator=emily)
    image5 = Image(path='https://i.pinimg.com/originals/9f/d5/85/9fd5852e85c80a6603b393b44c44f608.jpg', spot=fridaforever, creator=paul)
    image6 = Image(path='https://wonderlustinglynda.files.wordpress.com/2013/07/cept_streetart_love_will_tear_us_apart1.jpg?w=640', spot=lovewilltearusapart, creator=jamie)
    image7 = Image(path='https://4.bp.blogspot.com/-HVoKYrPN7hE/W3WkZsNYLAI/AAAAAAAAIzI/Cb9wmwLMgBcL88AtcWGd941SGYElZS4QwCLcBGAs/s1600/FANAKAPAN_12_HOOKEDBLOG_PHOTO_2018_MARK_RIGNEY.jpg', spot=upyours, creator=phil)
    image8 = Image(path='https://cdn.shopify.com/s/files/1/2258/3881/products/discover-london-s-street-art-by-mini-cooper-out-about-the-indytute-experience-gift-2610828378163_1024x1024_crop_center.jpg?v=1531342510', spot=robopolice, creator=hannah)
    image9 = Image(path='https://www.tilytravels.com/uploads/3/7/7/1/37712685/9150165.jpg', spot=snailart, creator=hannah)
    image10 = Image(path='https://i2.wp.com/inspiringcity.com/wp-content/uploads/2017/05/img_20170501_082323_008.jpg?w=1140&ssl=1', spot=tunnelart, creator=john)
    image11 = Image(path='https://media-cdn.tripadvisor.com/media/photo-s/07/41/27/b2/free-tours-by-foot.jpg', spot=funnybones, creator=sarah)
    image12 = Image(path='http://aeroarts.co.uk/wp-content/uploads/2016/06/aero_01_2016_03.jpg', spot=foxy, creator=jamie)
    image13 = Image(path='https://media.timeout.com/images/122265/image.jpg', spot=stickpeople, creator=ollie)
    image14 = Image(path='https://66.media.tumblr.com/7cd881836b11a85602b715e148051d06/tumblr_mwyr4nwe2x1r6wmavo1_1280.jpg', spot=animalcult, creator=robyn)
    image15 = Image(path='https://i.pinimg.com/originals/58/4d/b6/584db61b58bc7e0d115f60755458a7e5.jpg', spot=ninja, creator=jacob)
    image16 = Image(path='https://riotimesonline.com/wp-content/uploads/2014/09/bicicleta-photo-by-London-Graffiti.jpg', spot=lovewall, creator=dave)
    image17 = Image(path='https://mk0secretcitytrk62yu.kinstacdn.com/wp-content/uploads/2018/10/B.optional-end-1.1-Love-Lane-street-art-varies-low-res.jpg', spot=abstractwall, creator=paul)
    image18 = Image(path='https://s3.amazonaws.com/s.plague.io/upload/2016-04-04/dc21a1fc-7474-48d4-8d55-1bf2eca161f2.jpg', spot=nervouseddy, creator=ollie)
    image19 = Image(path='https://i.ebayimg.com/images/i/253092139136-0-1/s-l1000.jpg', spot=sadgirl, creator=robyn)
    image20 = Image(path='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX06l0a32uBcnkatLuchbN7oNwUg3huV9FV-IRgF3bKJTInaEQzA', spot=boardart, creator=ollie)
    image21 = Image(path='https://i.pinimg.com/originals/14/0e/44/140e44add09ec7a05700a311fe47cc1d.jpg', spot=lovelondon, creator=emily)
    image22 = Image(path='https://static.dezeen.com/uploads/2014/02/Phlegm-graffiti-exhibition-at-Howard-Griffin-Gallery_dezeen_sq.jpg', spot=noescape, creator=sarah)
    image23 = Image(path='https://d31fr2pwly4c4s.cloudfront.net/9/c/8/1078313_1_get-involved-in-a-street-art-workshop-at-boxpark_400.jpg', spot=highfive, creator=emily)
    image24 = Image(path='https://mypoppet.com.au/living/mp-content/uploads/2015/07/old-man-faces-london-art.jpg', spot=oldman, creator=paul)
    image25 = Image(path='https://jacquelinemhadel.files.wordpress.com/2015/01/bbib-147.jpg', spot=whiterabbit, creator=john)
    image26 = Image(path='http://www.scarlettentertainment.com/sites/default/files/img_Graffiti-Artist-London-Main.jpg', spot=winkwink, creator=ollie)
    image27 = Image(path='http://www.gerardpuxhe.com/wp-content/uploads/1fa16eda514711e3a28312f1f4f91bb3_8.jpg', spot=hendricks, creator=jacob)
    image28 = Image(path='https://i.pinimg.com/originals/a7/78/09/a77809fef0c508fdc40cd61aff32da56.jpg', spot=eyeseeyou, creator=sandra)
    image29 = Image(path='https://i.pinimg.com/originals/ef/52/ef/ef52efd1bca484bd126ae45466be8000.jpg', spot=colourmask, creator=nehal)
    image30 = Image(path='https://rmer1.com/wp-content/uploads/2017/06/magenta-skull-gardiff-graffiti-uk-web-rmer-cruelvapours-rmerism-1-uai-1125x1125.jpg', spot=pinkskull, creator=jamie)
    image31 = Image(path='https://s-i.huffpost.com/gen/1081881/thumbs/o-THATCHER-570.jpg?6', spot=turbothatcher, creator=dave)
    image32 = Image(path='http://www.bbc.co.uk/staticarchive/59a75d3522bba24ff587cf4dcfd3394f05e15bd4.jpg', spot=bigbird, creator=dave)
    image33 = Image(path='https://i2.wp.com/blog.artsper.com/wp-content/uploads/2015/07/banksy.png?fit=644%2C644&ssl=1', spot=plslike, creator=emily)
    image34 = Image(path='https://media1.s-nbcnews.com/j/newscms/2018_26/2478731/180627-banksy-paris-linda-mandog-square-540a_25376c35fb79a48845f9df3eb60caf84.social_share_1024x768_scale.jpg', spot=mananddog, creator=sandra)
    image35 = Image(path='http://4.bp.blogspot.com/-Utd2sTXzuBs/Uk1xpz1O3NI/AAAAAAAAE4Y/XAByLWkCdns/s1600/banksyny-558564037259684952_564287810.jpeg', spot=youcompleteme, creator=hannah)
    image36 = Image(path='http://coolsandfools.com/wp-content/uploads/2014/07/banksy-art-4.jpg', spot=destructart, creator=hannah)
    image37 = Image(path='https://artpil.com/wp-content/uploads/banksy-320.jpg', spot=search, creator=jamie)
    image38 = Image(path='http://cdn.shopify.com/s/files/1/0341/1101/products/banksy_gorilla-pink-mask_1200x1200.jpg?v=1529410042', spot=gorillamask, creator=jamie)
    image39 = Image(path='https://dynaimage.cdn.cnn.com/cnn/q_auto,w_412,c_fill,g_auto,h_412,ar_1:1/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F131014154324-11-banksy.jpg', spot=thekiss, creator=dave)
    image40 = Image(path='https://blog-and-the-city.com/wp-content/uploads/2017/04/photo-a-la-une-banksy-1-292x292.jpg?x20934', spot=plslike, creator=nehal)
    image41 = Image(path='https://i.pinimg.com/originals/42/34/19/423419195edcb94332e6a7285cbe9cb5.jpg', spot=theaffair, creator=hannah)
    image42 = Image(path='https://static.greatbigcanvas.com/images/square/estock/england-great-britain-london-london-borough-of-hackney-shoreditch-graffiti,2424250.jpg?max=540?max=220', spot=octoelephant, creator=joelle)
    image43 = Image(path='https://strawberrytours.com/images/LondonStreetArtTour/Highlights/Zabou.jpg', spot=toxic, creator=john)
    image44 = Image(path='https://frankiebeane.files.wordpress.com/2017/01/helovesnot.png?w=833', spot=helovesme, creator=nehal)
    image45 = Image(path='https://media2.trover.com/T/4ff0b9c74d62023560000002/fixedw_large_2x.jpg', spot=theaffair, creator=phil)
    image46 = Image(path='http://4.bp.blogspot.com/-lxszw-QAUxA/U79KT5j3JjI/AAAAAAAAHV0/1VQdqqQy2Bw/s1600/Alice+in+Wonderland.jpg', spot=alice, creator=emily)
    image47 = Image(path='https://i2.wp.com/hilarystyle.me/wp-content/uploads/2018/12/Brick-Lane-Zabou-London-England-2.jpg?w=386&h=386&crop=1&ssl=1', spot=toxic, creator=dave)
    image48 = Image(path='https://i.pinimg.com/originals/b4/64/65/b46465a28dac9c29c74022205d8bfc13.jpg', spot=coolhat, creator=nehal)
    image49 = Image(path='https://2.bp.blogspot.com/-KOq2QIcXjFM/WhgLsImYWVI/AAAAAAAAKPg/5TC7vPlonOsh9tfKCupQfllbkzlLeUKjQCLcBGAs/s1600/graffiti%2Bgarden%2B02.jpg', spot=threed, creator=phil)
    image50 = Image(path='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHhNOr3PFbFh-PXbzGwZRFHLYcxqdT15gfc3IX2aCwZBAWUVIL', spot=theaffair, creator=phil)
    # image55 = Image(path='https://www.handpicked.org/api/image?width=500&url=http%3A%2F%2F40.media.tumblr.com%2Ftumblr_mci08t6mVA1r9zqkpo1_1280.jpg', spot=bolt, creator=dave)
    image56 = Image(path='https://1.bp.blogspot.com/-BwPBvAPDgqw/WI-VV0R9API/AAAAAAAAG20/ZnQYZvcTnFcal9s-mTUb9_KbhKFVk8bOgCLcB/s1000/Ant_Carver_08_HOOKEDBLOG_PHOTO_%25C2%25A92017_MARK_RIGNEY.jpg', spot=truecolours, creator=paul)
    image57 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2018/09/p1290745.jpg?w=920&h=920&crop=1', spot=cartoonheaven, creator=john)
    image58 = Image(path='https://i.pinimg.com/originals/6e/52/55/6e5255099ecf14671f1bf1787876ac52.jpg', spot=checkmate, creator=nehal)
    image59 = Image(path='https://www.visualwaste.co.uk/wp-content/uploads/2016/02/image1.jpeg', spot=thethinker, creator=ollie)
    image60 = Image(path='https://www.thebc-club.com/wp-content/uploads/2017/05/shoreditch-street-art-4.jpg', spot=teardownthiswall, creator=joelle)
    image61 = Image(path='https://www.graffitistreet.com/wp-content/uploads/2016/03/east-london-rebels-dface-rebel-alliance.jpg', spot=wackyracers, creator=sarah)
    image62 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2018/12/P1310996.jpg?w=920&h=920&crop=1', spot=tizer, creator=hannah)
    image63 = Image(path='https://i.pinimg.com/originals/53/66/7c/53667cce10a356cc3d7fb876c051542b.jpg', spot=ghostrider, creator=paul)
    image64 = Image(path='https://i.pinimg.com/originals/2a/ed/68/2aed68e078a069c7fc375e3bacfd3a95.jpg', spot=thepowerofgirl, creator=jamie)
    # image65 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2016/05/p1460193.jpg?w=920&h=920&crop=1', spot=thethreegirls, creator=sarah)
    image66 = Image(path='https://media-cdn.tripadvisor.com/media/photo-s/14/68/66/f4/photo9jpg.jpg', spot=skulls, creator=phil)
    image67 = Image(path='https://media-cdn.tripadvisor.com/media/photo-s/0c/5e/12/d3/street-art-tour-london.jpg', spot=cartoonheaven, creator=phil)
    image68 = Image(path='http://www.commontoff.com/wp-content/uploads/2016/10/beasts-wall-1440x1440.jpg', spot=roar, creator=joelle)
    image69 = Image(path='https://c1.staticflickr.com/6/5529/30810768361_496dcdefde_b.jpg', spot=thecircus, creator=ollie)
    image70 = Image(path='https://lookup.london/wp-content/uploads/2016/12/Photo-17-12-2016-10-35-36-1024x1024.jpg', spot=thewolf, creator=sarah)
    image71 = Image(path='https://pbs.twimg.com/media/DnuGQbfX4AAA4vH.jpg', spot=paintwithlove, creator=adam)
    image72 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2016/04/p1440196.jpg?w=920&h=920&crop=1', spot=allthecolours, creator=dave)
    image73 = Image(path='https://nicolkyp.files.wordpress.com/2017/10/1.jpg?w=1400', spot=scarymary, creator=jacob)
    image74 = Image(path='https://farm5.static.flickr.com/4823/44458920500_cd3c53492c_b.jpg', spot=faces, creator=sandra)
    image75 = Image(path='https://res.cloudinary.com/fleetnation/image/private/c_fit,w_1120/g_south,l_text:style_gothic2:%C2%A9%20Stockimo,o_20,y_10/g_center,l_watermark4,o_25,y_50/v1482999044/hoqlnnmfzgih0sxi5kgs.jpg', spot=trumpsays, creator=jamie)
    image76 = Image(path='https://static.wixstatic.com/media/8aa835_59b371901c6a4247bce4c01c1307d6de~mv2.jpg/v1/fill/w_429,h_429,al_c,q_80,usm_0.66_1.00_0.01/8aa835_59b371901c6a4247bce4c01c1307d6de~mv2.jpg', spot=wings, creator=joelle)
    image77 = Image(path='https://static1.squarespace.com/static/53d6b68ae4b01cdbaa06f1df/t/56406c1ce4b0bff850432b1f/1447062631100/', spot=faces, creator=jamie)
    image78 = Image(path='https://i.pinimg.com/originals/06/fd/e6/06fde63d13a7c8c995975d07ada9280d.jpg', spot=lovewall, creator=emily)
    image79 = Image(path='https://www.thingstodoinlondon.com/wp-content/uploads/f-graffiti-in-shoreditch.jpg', spot=cowboy, creator=hannah)
    image80 = Image(path='http://ollystudio.co.uk/wp-content/uploads/2013/01/tumblr_mgbt42TroQ1rla4poo1_1280.jpg', spot=whiterabbit, creator=ollie)
    image81 = Image(path='https://i.pinimg.com/originals/d1/c8/2b/d1c82bf93677ce022e251b5f08540fe9.jpg', spot=oldlondon, creator=hannah)
    image82 = Image(path='https://images01.foap.com/images/7532170d-7b9f-4b50-8cfb-fae7b8ddc103/where-you-headed-today-graffiti-spotted-at-bricklane-shoreditch.jpg?filename=w1280&dw=960', spot=boardmeeting, creator=john)
    image83 = Image(path='https://upload.wikimedia.org/wikipedia/commons/6/60/Graffiti_in_Shoreditch%2C_London_-_Time_Machine_by_Paul_Don_Smith_%289425007440%29.jpg', spot=timeisanillusion, creator=jamie)
    image84 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2018/06/p1180976.jpg?w=920&h=920&crop=1', spot=peace, creator=nehal)
    image85 = Image(path='https://media-cdn.tripadvisor.com/media/photo-s/0b/32/89/74/shoreditch-london-may.jpg', spot=zomg, creator=nehal)
    image86 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2017/07/p1910910.jpg?w=920&h=920&crop=1', spot=bull, creator=robyn)
    image87 = Image(path='https://cdn1.gifts.co.uk/media/catalog/product/cache/6/image/1104x/040ec09b1e35df139433887a97daa66f/s/t/street-art-photography-tour-gifts-co-uk_uk1405-1c58219b.jpg', spot=iloveshoreditch, creator=phil)
    image88 = Image(path='https://66.media.tumblr.com/bcf8074227f6255234143a6f53fc4605/tumblr_nrp5fmreYS1ruo0x9o1_640.jpg', spot=murdershewrote, creator=ollie)
    image89 = Image(path='https://www.graffitistreet.com/graffitistreet-underground-pre-group-show-on-the-streets-of-london/joachim-hunto-clare-street-bethnal-green/', spot=dearsister, creator=paul)
    image90 = Image(path='https://scontent-ort2-1.cdninstagram.com/vp/d47f13042c61aa985f1859761a020acf/5D20EF21/t51.2885-15/e35/s480x480/52837118_319105325475073_355636089609318931_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com', spot=coolbeans, creator=jamie)
    image91 = Image(path='https://www.thestyledivision.com/wp-content/uploads/2017/03/shoreditch-london-street-art-graffiti-things-to-do-14.jpg', spot=highnoon, creator=phil)
    image92 = Image(path='https://i0.wp.com/inspiringcity.com/wp-content/uploads/2013/01/wpid-img_20130120_132109.jpg', spot=scarymary, creator=emily)
    image93 = Image(path='https://scontent-lga3-1.cdninstagram.com/vp/7068ff889028c10231e3453de114694d/5CF2C5BA/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/49592635_2618766504807209_1197492061280471951_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com', spot=snowinmay, creator=ollie)
    image94 = Image(path='https://66.media.tumblr.com/1f869d17b619d1a2cda8a3af31f6b6e0/tumblr_o68ozwvZKm1v7slcoo1_1280.jpg', spot=kingsguard, creator=emily)
    image95 = Image(path='https://1.bp.blogspot.com/-czLcJFPCy54/XC6LNk9jjVI/AAAAAAAAJQ0/bowDURhKO5UNqpB7RIgg3j-2EFG9edr7QCLcBGAs/s1600/Minty_Hookedblog_Photo_2018_%25C2%25A9Mark_Rigney.jpg', spot=doublelove, creator=dave)
    image96 = Image(path='https://whatskatiedoing.com/wp-content/uploads/2016/06/IMG_5208.jpg', spot=dontshoot, creator=adam)
    image97 = Image(path='https://i0.wp.com/theoccasionaltraveller.com/wp-content/uploads/2014/07/London-Street-Art-Penguin.jpg?resize=600%2C600', spot=tongueemoji, creator=sandra)
    image98 = Image(path='https://pbs.twimg.com/media/DKKJ_olWAAAzcdz.jpg', spot=thehand, creator=robyn)
    image99 = Image(path='https://media2.trover.com/T/4fbbbe04457a08049b0000ff/fixedw_large_4x.jpg', spot=londonpleasuregardens, creator=jacob)
    image100 = Image(path='https://jgtravels.files.wordpress.com/2017/09/d71_2882.jpg', spot=toxic, creator=john)
    image101 = Image(path='https://graffitibanksy99.com/wp-content/uploads/2017/06/shoreditch-street-art-why-shoreditch-street-art-is-basically-traditional-fine-art-c2b7-look.jpg', spot=dontshoot, creator=sandra)
    image102 = Image(path='https://i.imgur.com/cU8ehma.jpg', spot=ec4, creator=ollie)
    image103 = Image(path='https://c1.staticflickr.com/5/4356/35952401353_28c93059f0_b.jpg', spot=entwined, creator=jacob)
    image104 = Image(path='https://scontent.cdninstagram.com/vp/47ba9b5c1306786f9d2c1002d60c61b2/5D14BCAC/t51.2885-15/e35/c0.135.1080.1080/s480x480/51917137_344055742880163_6910222406121663763_n.jpg?_nc_ht=scontent-sea1-1.cdninstagram.com', spot=heartandmind, creator=jacob)
    image105 = Image(path='https://farm8.static.flickr.com/7582/15976110578_02be05ec76_b.jpg', spot=natureheart, creator=phil)
    image106 = Image(path='https://66.media.tumblr.com/8a5ecfd5594ddcf50222a9f868522686/tumblr_o6hp28tZZS1v7slcoo1_1280.jpg', spot=sunrise, creator=sarah)
    image107 = Image(path='https://s3-media4.fl.yelpcdn.com/bphoto/P6fbV2S9FGJUid0yTEUiLA/o.jpg', spot=comingautumn, creator=paul)
    image108 = Image(path='https://i.redd.it/u2d1e5g4nii21.jpg', spot=brexitcellent, creator=ollie)
    image109 = Image(path='https://alternativeadventurers.files.wordpress.com/2016/08/2016-08-05-17-15-35-hdr.jpg?w=396&h=396&crop=1', spot=mystic, creator=jamie)
    image110 = Image(path='https://londoncallingblogdotnet.files.wordpress.com/2017/08/p1000553.jpg?w=920&h=920&crop=1', spot=lady, creator=phil)
    image111 = Image(path='http://aeroarts.co.uk/wp-content/uploads/2015/04/BRIX_1.jpg', spot=ourheartishere, creator=dave)
    image112 = Image(path='http://aeroarts.co.uk/wp-content/uploads/2015/04/mrcenz-02.jpg', spot=intergalactic, creator=sandra)
    image113 = Image(path='http://aeroarts.co.uk/wp-content/uploads/2015/04/SKY_ROO1.jpg', spot=savebrixton, creator=nehal)

    comment1 = Comment(content='I love this place', spot=upyours, creator=sarah)
    comment2 = Comment(content='So so cool', spot=swanstreet, creator=sarah)

    db.session.add(upyours)
    db.session.add(swanstreet)
    db.session.add(bees)
    db.session.add(squirrelnest)
    db.session.add(fridaforever)
    db.session.add(lovewilltearusapart)
    db.session.add(robopolice)
    db.session.add(snailart)
    db.session.add(tunnelart)
    db.session.add(funnybones)
    db.session.add(foxy)
    db.session.add(stickpeople)
    db.session.add(animalcult)
    db.session.add(ninja)
    db.session.add(lovewall)
    db.session.add(abstractwall)
    db.session.add(nervouseddy)
    db.session.add(sadgirl)
    db.session.add(boardart)
    db.session.add(lovelondon)
    db.session.add(noescape)
    db.session.add(highfive)
    db.session.add(oldman)
    db.session.add(whiterabbit)
    db.session.add(winkwink)
    db.session.add(hendricks)
    db.session.add(eyeseeyou)
    db.session.add(colourmask)
    db.session.add(pinkskull)
    db.session.add(turbothatcher)
    db.session.add(bigbird)
    db.session.add(plslike)
    db.session.add(mananddog)
    db.session.add(youcompleteme)
    db.session.add(destructart)
    db.session.add(search)
    db.session.add(gorillamask)
    db.session.add(thekiss)
    db.session.add(theaffair)
    db.session.add(octoelephant)
    db.session.add(helovesme)
    db.session.add(alice)
    db.session.add(toxic)
    db.session.add(coolhat)
    db.session.add(threed)
    # db.session.add(bolt)
    db.session.add(truecolours)
    db.session.add(cartoonheaven)
    db.session.add(checkmate)
    db.session.add(thethinker)
    db.session.add(teardownthiswall)
    db.session.add(wackyracers)
    db.session.add(tizer)
    db.session.add(ghostrider)
    db.session.add(thepowerofgirl)
    # db.session.add(thethreegirls)
    db.session.add(skulls)
    db.session.add(roar)
    db.session.add(thecircus)
    db.session.add(thewolf)
    db.session.add(paintwithlove)
    db.session.add(allthecolours)
    db.session.add(scarymary)
    db.session.add(faces)
    db.session.add(trumpsays)
    db.session.add(wings)
    db.session.add(cowboy)
    db.session.add(oldlondon)
    db.session.add(boardmeeting)
    db.session.add(timeisanillusion)
    db.session.add(peace)
    db.session.add(zomg)
    db.session.add(bull)
    db.session.add(iloveshoreditch)
    db.session.add(murdershewrote)
    db.session.add(dearsister)
    db.session.add(coolbeans)
    db.session.add(highnoon)
    db.session.add(snowinmay)
    db.session.add(kingsguard)
    db.session.add(doublelove)
    db.session.add(dontshoot)
    db.session.add(tongueemoji)
    db.session.add(thehand)
    db.session.add(londonpleasuregardens)
    db.session.add(ec4)
    db.session.add(entwined)
    db.session.add(heartandmind)
    db.session.add(natureheart)
    db.session.add(sunrise)
    db.session.add(comingautumn)
    db.session.add(brexitcellent)
    db.session.add(mystic)
    db.session.add(lady)
    db.session.add(ourheartishere)
    db.session.add(intergalactic)
    db.session.add(savebrixton)

    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.add(image9)
    db.session.add(image10)
    db.session.add(image11)
    db.session.add(image12)
    db.session.add(image13)
    db.session.add(image14)
    db.session.add(image15)
    db.session.add(image16)
    db.session.add(image17)
    db.session.add(image18)
    db.session.add(image19)
    db.session.add(image20)
    db.session.add(image21)
    db.session.add(image22)
    db.session.add(image23)
    db.session.add(image24)
    db.session.add(image25)
    db.session.add(image26)
    db.session.add(image27)
    db.session.add(image28)
    db.session.add(image29)
    db.session.add(image30)
    db.session.add(image31)
    db.session.add(image32)
    db.session.add(image33)
    db.session.add(image34)
    db.session.add(image35)
    db.session.add(image36)
    db.session.add(image37)
    db.session.add(image38)
    db.session.add(image39)
    db.session.add(image40)
    db.session.add(image41)
    db.session.add(image42)
    db.session.add(image43)
    db.session.add(image44)
    db.session.add(image45)
    db.session.add(image46)
    db.session.add(image47)
    db.session.add(image48)
    db.session.add(image49)
    db.session.add(image50)
    # db.session.add(image55)
    db.session.add(image56)
    db.session.add(image57)
    db.session.add(image58)
    db.session.add(image59)
    db.session.add(image60)
    db.session.add(image61)
    db.session.add(image62)
    db.session.add(image63)
    db.session.add(image64)
    # db.session.add(image65)
    db.session.add(image66)
    db.session.add(image67)
    db.session.add(image68)
    db.session.add(image69)
    db.session.add(image70)
    db.session.add(image71)
    db.session.add(image72)
    db.session.add(image73)
    db.session.add(image74)
    db.session.add(image75)
    db.session.add(image76)
    db.session.add(image77)
    db.session.add(image78)
    db.session.add(image79)
    db.session.add(image80)
    db.session.add(image81)
    db.session.add(image82)
    db.session.add(image83)
    db.session.add(image84)
    db.session.add(image85)
    db.session.add(image86)
    db.session.add(image87)
    db.session.add(image88)
    db.session.add(image89)
    db.session.add(image90)
    db.session.add(image91)
    db.session.add(image92)
    db.session.add(image93)
    db.session.add(image94)
    db.session.add(image95)
    db.session.add(image96)
    db.session.add(image97)
    db.session.add(image98)
    db.session.add(image99)
    db.session.add(image100)
    db.session.add(image101)
    db.session.add(image102)
    db.session.add(image103)
    db.session.add(image104)
    db.session.add(image105)
    db.session.add(image106)
    db.session.add(image107)
    db.session.add(image108)
    db.session.add(image109)
    db.session.add(image110)
    db.session.add(image111)
    db.session.add(image112)
    db.session.add(image113)

    db.session.add(comment1)
    db.session.add(comment2)

    db.session.commit()
