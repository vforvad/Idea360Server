import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import yaml
import nose

from app import create_app, db

def load_secrets():
    if os.path.isfile('secrets.yaml'):
        with open('secrets.yaml') as stream:
            f = yaml.load(stream)
            for k, v in f.items():
                os.environ[k] = v

load_secrets()
app = create_app(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """ Run tests without coverage """
    args = ['--with-spec', '--spec-color']
    nose.main()

if __name__ == '__main__':
    manager.run()
