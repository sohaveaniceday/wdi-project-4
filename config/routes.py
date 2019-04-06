from app import app
from controllers import spots, categories, auth

app.register_blueprint(spots.api, url_prefix='/api')
app.register_blueprint(categories.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
