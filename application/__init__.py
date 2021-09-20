from flask import Flask
import os

from dotenv import load_dotenv
load_dotenv()

from .blueprints.routes import route
from .blueprints.endpts import endpt

from application.middleware.extensions import mongo

# Application Factory
def create_app(test_config=None):
    # Create Flask Application
    app = Flask(__name__, instance_relative_config=True)

    # Set Default configs
    app.config.from_mapping(SECRET_KEY = 'dev')

    # Set config based on test or not
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)
    
    prefix = f'/{app.config["APP_NAME"]}/api'

    # Database Connection
    mongo.init_db(app)
    mongo.make_connection()
    mongo.check_connection()

    # Links blueprints
    app.register_blueprint(route)
    app.register_blueprint(endpt, url_prefix=prefix)

    return app
