from app.api import api_v1
from flask import request, g
from flask_restful import Resource, abort
from app.models import User, Company

from .users import UsersResource
from .registrations import RegistrationsResource
from .current_user import CurrentUserResource
from .authorization import AuthorizationResource
from .companies import CompaniesResource
from .company import CompanyResource

api_v1.add_resource(UsersResource, '/users')
api_v1.add_resource(RegistrationsResource, '/registrations')
api_v1.add_resource(AuthorizationResource, '/authorizations')
api_v1.add_resource(CurrentUserResource, '/users/current')
api_v1.add_resource(CompaniesResource, '/companies')
api_v1.add_resource(CompanyResource, '/companies/<company_id>')
