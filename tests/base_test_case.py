import unittest
from app import create_app, db

class BaseTestCase(unittest.TestCase):
    def __call__(self, result=None):
        try:
            self._pre_setup()
            super(BaseTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def _pre_setup(self):
        self.app = create_app(config_name="test")
        self.client = self.app.test_client

        with self.app.app_context():
            # create all tables
            db.create_all()

    def _post_teardown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
