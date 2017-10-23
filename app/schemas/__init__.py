from flask_marshmallow import Marshmallow
ma = Marshmallow()

from .user import UserSchema, user_schema, users_schema
