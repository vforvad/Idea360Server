from . import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DB_NAME = 'idea360'
    SECRET_KEY = os.environ.get('JWT_SECRET')
    SQLALCHEMY_ACCESS = 'postgresql://postgres:{}@postgres'.format(
        os.environ.get('POSTGRES_PASSWORD')
    )
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@postgres/{}'.format(
        os.environ.get('POSTGRES_PASSWORD'), DB_NAME
    )
