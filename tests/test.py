import unittest
from base_test_case import BaseTestCase

class TestExample(BaseTestCase):

    def test_success(self):
        self.assertEqual(1 + 1, 2)
