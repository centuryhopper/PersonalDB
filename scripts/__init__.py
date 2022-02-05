from flask import Flask

from .extensions import mongo
from .main import main

def create_app(config_object='scripts.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(main)
    mongo.init_app(app)

    return app
