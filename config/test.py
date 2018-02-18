from . import BaseConfig, os

class TestConfig(BaseConfig):
    TESTING = True
    DEBUG = False
    DB_NAME = 'idea360_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@postgres/{}'.format(
        os.environ.get('POSTGRES_PASSWORD'), DB_NAME
    )
