from flask_restful import Resource
from app.models import User
from app.schemas import users_schema
from flask import make_response

class UsersResource(Resource):
    """ User API resource """

    def get(self):
        users = User.query.all()
        return { 'users': users_schema.dump(users).data }
