from flask_restful import Resource, reqparse
from app.models import db, User
from app.schemas import user_schema
import ipdb

class RegistrationsResource(Resource):
    """ Registration resource """

    def post(self):
        """ receive user params and create a new user """

        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('password_confirmation', type=str, required=True)

        params = parser.parse_args(strict=True)
        user = User(email=params['email'], password=params['password'])
        db.session.add(user)
        db.session.commit()
        return { 'user': user_schema.dump(user).data }
