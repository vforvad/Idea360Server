from wtforms import Form, fields, validators
import sqlalchemy

from app.models import db, User
from app.services import encode_user

from .registration import RegistrationForm
