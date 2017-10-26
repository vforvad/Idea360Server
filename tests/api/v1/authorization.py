from . import BaseTestCase, json, UserFactory

class AuthorizationViewTest(BaseTestCase):
    """ AuthorizationResource view test """

    def setUp(self):
        """ Setting up test dependencies """

        self.user = UserFactory()
        self.form_data = {
            'email': self.user.email,
            'password': '123456'
        }

    def test_success_authorization(self):
        """ Test success user authorization """

        res = self.client().post(
            '/api/v1/authorizations', data=json.dumps(self.form_data), content_type='application/json'
        )
        result = json.loads(res.data.decode())
        assert 'token' in result

    def test_failed_registration(self):
        """ Test failed authorization """

        res = self.client().post(
            '/api/v1/authorizations', data=json.dumps({}), content_type='application/json'
        )
        
        result = json.loads(res.data.decode())
        assert res.status_code == 400
        assert 'errors' in result
