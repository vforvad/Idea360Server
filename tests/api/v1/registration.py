from tests.base_test_case import BaseTestCase
import json
import ipdb

class RegistrationViewTest(BaseTestCase):
    """ Registration view test """

    def setUp(self):
        """ Setting up test dependencies """

        self.form_data = {
            'email': 'example@mail.com',
            'password': 'password',
            'password_confirmation': 'password'
        }

    def test_success_registration(self):
        """ Test success registration """

        res = self.client().post(
            '/api/v1/registrations', data=json.dumps(self.form_data), content_type='application/json'
        )
        result = json.loads(res.data.decode())
        assert 'token' in result

    def test_failed_registration(self):
        """ Test failed registration """

        res = self.client().post(
            '/api/v1/registrations', data=json.dumps({}), content_type='application/json'
        )
        result = json.loads(res.data.decode())
        assert 'errors' in result
