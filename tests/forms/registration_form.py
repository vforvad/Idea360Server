from . import BaseTestCase, UserFactory
from app.forms.registration import RegistrationForm

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

    def test_user_succesfully_created(self):
        """ Test success creation of user """

        form = RegistrationForm(data={
            'email': 'vforvad@gmail.com',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        form.submit()
        self.assertTrue(hasattr(form, 'token'))


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
