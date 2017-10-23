from app.api import api_v1
from flask import request, g
from flask_restful import Resource, abort
from app.models import User

from .users import UsersResource
from .registrations import RegistrationsResource
from .current_user import CurrentUserResource

api_v1.add_resource(UsersResource, '/users')
api_v1.add_resource(RegistrationsResource, '/registrations')
api_v1.add_resource(CurrentUserResource, '/users/current')
