from wtforms import Form, fields, validators
import sqlalchemy

from app.models import db, User, Company
from app.services import encode_user

from .registration import RegistrationForm
from .authorization import AuthorizationForm
from .company import CompanyForm
