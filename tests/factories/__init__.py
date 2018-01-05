from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence
from factory.alchemy import SQLAlchemyOptions
from sqlalchemy.orm import scoped_session, sessionmaker
from faker import Faker
from app.models import db

fake = Faker()
Session = scoped_session(sessionmaker())
from .user_factory import UserFactory
from .company_factory import CompanyFactory
