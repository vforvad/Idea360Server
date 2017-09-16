from flask_restful import Resource

class UsersResource(Resource):
    """ User API resource """

    def get(self):
        return { 'users': [] }
