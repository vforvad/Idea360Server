import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml
from colour_runner.runner import ColourTextTestRunner
from colour_runner.result import ColourTextTestResult
from config import app_config
from app import create_app, db
import ipdb


app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test(test_name=None):
    """ Run tests without coverage """

    if test_name is None:
        tests = unittest.TestLoader().discover('tests')
    else:
        tests = unittest.TestLoader().loadTestsFromName(test_name)
    ColourTextTestRunner(verbosity=2).run(tests)

@manager.command
def createdb(name):
    """ Create database with specific name """

    try:
        config_class = app_config[name]
        pg_engine = create_engine(config_class.SQLALCHEMY_ACCESS)
        session = sessionmaker(bind=pg_engine)()
        session.connection().connection.set_isolation_level(0)
        session.execute('CREATE DATABASE {}'.format(config_class.DB_NAME))
        session.connection().connection.set_isolation_level(1)
    except KeyError:
        print('Environment of type {} does not exist'.format(name))

if __name__ == '__main__':
    manager.run()
