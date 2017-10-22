from . import BaseTestCase
from app.forms.registration import RegistrationForm
from tests.factories import UserFactory
import ipdb

class RegistrationFormTest(BaseTestCase):
    """ RegistrationForm tests  """

    def test_success_form_validation(self):
        """ Test success form validation """

        form = RegistrationForm(data={
            'email': 'vforvad@gmail.com',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        self.assertTrue(form.validate())

    def test_failed_form_validation(self):
        """ Test failed form validation """

        form = RegistrationForm()
        self.assertFalse(form.validate())

    def test_user_already_exists(self):
        """ Test failure if user already exists """

        user = UserFactory()
        form = RegistrationForm(data={
            'email': user.email,
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        self.assertFalse(form.submit())
        assert 'user' in form.errors
