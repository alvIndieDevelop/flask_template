from flask_restx import Resource, Namespace

ping = Namespace('ping', description='Ping related operations')

@ping.route('/')
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }
