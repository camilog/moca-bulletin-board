from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

import json

# Create flask app
application = Flask(__name__)

# Cache configuration
application.config['CACHE_TYPE'] = 'redis'
application.config['CACHE_REDIS_HOST'] = json.load(application.open_resource('config.json'))['redis']['redis_host']
application.cache = Cache(application)

# Load the default configuration
application.config.from_object("config.DefaultConfig")

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)

from app import public
from app import data
