from . import Resource, User
from app.schemas import users_schema

class UsersResource(Resource):
    """ User API resource """

    def get(self):
        users = User.query.all()
        return { 'users': users_schema.dump(users).data }
