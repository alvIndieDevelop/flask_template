from flask import Blueprint
from flask_restx import Api

blueprint_app_v1 = Blueprint('app_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(blueprint_app_v1, version='1.0', title='API v1', description='API v1')

# import resources
from app.v1.router.ping import ping

# routes
api_v1.add_namespace(ping)