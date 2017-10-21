from . import BaseTestCase
from app.forms.registration import RegistrationForm
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
