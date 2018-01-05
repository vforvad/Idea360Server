from flask import request, g
from app.models import User
from functools import wraps
import os
import jwt
import ipdb

AUTH_HEADER = 'Authorization'

def authenticate(func):
    """ Authenticate user wrapper """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if request.headers[AUTH_HEADER]:
                g.current_user = decode_user(request.headers[AUTH_HEADER])
                return func(*args, **kwargs)
            else:
                return { 'error': 'Unauthorized' }, 401
        except (KeyError, jwt.exceptions.DecodeError):
            return { 'error': 'Unauthorized' }, 401
    return wrapper

def encode_user(user):
    """ Encode user id to token """

    return jwt.encode({'id': user.id}, _get_jwt_secret(), 'HS256')

def decode_user(token):
    """ Receive user by givin token  """

    user_info = jwt.decode(
        request.headers[AUTH_HEADER],
        _get_jwt_secret(), algorithms=['HS256']
    )
    return User.query.get(user_info['id'])

def _get_jwt_secret():
    """ return JWT secret env parameter """

    return os.environ.get('JWT_SECRET')
