from app.api import api_v1
from .users import UsersResource

api_v1.add_resource(UsersResource, '/users')
