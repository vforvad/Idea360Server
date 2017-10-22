from . import Resource, request, abort, g, User
from functools import wraps
import os
import jwt
import ipdb

AUTH_HEADER = 'Authorization'

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if request.headers[AUTH_HEADER]:
                secret_token = os.environ['JWT_SECRET']
                user_info = jwt.decode(request.headers[AUTH_HEADER], secret_token, algorithms=['HS256'])
                g.current_user = User.query.get(user_info['id'])
                return func(*args, **kwargs)
            else:
                return { 'error': 'Unauthorized' }, 401
        except:
            return { 'error': 'Unauthorized' }, 401
    return wrapper

class CurrentUserResource(Resource):
    """ Current User resource """

    method_decorators = [authenticate]

    def get(self):
        return { 'current_user': g.current_user.id }
