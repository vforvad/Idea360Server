import unittest
from app import create_test_app, db
import ipdb

class BaseTestCase(unittest.TestCase):
    def __call__(self, result=None):
        try:
            self._pre_setup()
            super(BaseTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def _pre_setup(self):
        self.app = create_test_app()
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db
        db.create_all()

    def _post_teardown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
