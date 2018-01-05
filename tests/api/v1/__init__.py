from tests.base_test_case import BaseTestCase
from app.models import Company
from app.services import encode_user, AUTH_HEADER
import json
from tests.factories import UserFactory, CompanyFactory

from .registration import RegistrationViewTest
from .authorization import AuthorizationViewTest
from .companies import CompaniesViewTest
