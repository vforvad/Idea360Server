from app.api import api_v1
from .users import UsersResource
from .registrations import RegistrationsResource

api_v1.add_resource(UsersResource, '/users')
api_v1.add_resource(RegistrationsResource, '/registrations')
