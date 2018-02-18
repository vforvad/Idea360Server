from . import BaseTestCase, UserFactory

from app.forms.authorization import AuthorizationForm

class AuthorizationFormTest(BaseTestCase):
    """ AuthorizationForm tests """

    def setUp(self):
        """ Setting up testing dependencies """

        self.user = UserFactory()

    def test_success_form_valid(self):
        """ Test success form validation """

        form = AuthorizationForm(params={
            'email': self.user.email,
            'password': '123456'
        })
        self.assertTrue(form.is_valid())

    def test_failed_form_valid(self):
        """ Test failed form validation """
        form = AuthorizationForm(params={})
        self.assertFalse(form.is_valid())

    def test_success_authorization(self):
        """ Test success authorization """

        form = AuthorizationForm(params={
            'email': self.user.email,
            'password': '123456'
        })
        form.submit()
        self.assertTrue(hasattr(form, 'token'))

    def test_failed_authorization(self):
        """ Test failed authorization """

        form = AuthorizationForm(params={
            'email': self.user.email,
            'password': ''
        })
        form.submit()
        assert 'password' in form.errors

    def test_user_abascent(self):
        """ Test form errors if such user is not exists """

        form = AuthorizationForm(params={
            'email': self.user.email,
            'password': 'example'
        })
        form.submit()
        assert 'user' in form.errors
