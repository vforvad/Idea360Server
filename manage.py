import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import yaml
from colour_runner.runner import ColourTextTestRunner
from colour_runner.result import ColourTextTestResult

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
def test(test_name=None):
    """ Run tests without coverage """
    if test_name is None:
        tests = unittest.TestLoader().discover('./tests')
    else:
        tests = unittest.TestLoader().loadTestsFromName(test_name)
    result = ColourTextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
