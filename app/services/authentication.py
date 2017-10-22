from flask import request, g
from app.models import User
from functools import wraps
import os
import jwt

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
