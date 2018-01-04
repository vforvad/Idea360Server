import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
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


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    DB_NAME = 'idea360_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@postgres/{}'.format(
        os.environ.get('POSTGRES_PASSWORD'), DB_NAME
    )

app_config = {
    'development': DevelopmentConfig,
    'test': TestingConfig
}
