from . import BaseTestCase
from app.forms.registration import RegistrationForm
import ipdb

class RegistrationFormTest(BaseTestCase):

    def test_success_form_validation(self):
        form = RegistrationForm(data={
            'email': 'vforvad@gmail.com',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        self.assertTrue(form.validate())
