from app import app
from controllers import spots, categories, auth, artists, users

app.register_blueprint(spots.api, url_prefix='/api')
app.register_blueprint(categories.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
app.register_blueprint(artists.api, url_prefix='/api')
app.register_blueprint(users.api, url_prefix='/api')
