from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app(config_name='dev'):
    from config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # cors
    cors.init_app(app, origins='*', allow_headers=['content-type'], supports_credentials=True)

    # register blueprints
    from app.v1.api_v1 import blueprint_app_v1
    app.register_blueprint(blueprint_app_v1)

    return app
