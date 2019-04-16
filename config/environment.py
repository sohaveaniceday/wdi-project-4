import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/spots')
secret = os.getenv('SECRET', 'shhh its a secret')
