from . import BaseTestCase, UserFactory
from app.forms.registration import RegistrationForm

class RegistrationFormTest(BaseTestCase):
    """ RegistrationForm tests  """

    def test_success_form_validation(self):
        """ Test success form validation """

        form = RegistrationForm(params={
            'email': 'vforvad@gmail.com',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        self.assertTrue(form.is_valid())

    def test_failed_form_validation(self):
        """ Test failed form validation """

        form = RegistrationForm()
        self.assertFalse(form.is_valid())

    def test_user_succesfully_created(self):
        """ Test success creation of user """

        form = RegistrationForm(params={
            'email': 'vforvad@gmail.com',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        form.submit()
        self.assertTrue(hasattr(form, 'token'))


    def test_user_already_exists(self):
        """ Test failure if user already exists """

        user = UserFactory()
        form = RegistrationForm(params={
            'email': user.email,
            'password': 'Altair_69',
            'password_confirmation': 'Altair_69'
        })
        self.assertFalse(form.submit())
        assert 'user' in form.errors

    def test_failed_if_password_does_not_matches(self):
        """ Test failure if passwords are not matched """

        form = RegistrationForm(params={
            'email': 'awdawd@mail.ru',
            'password': 'Altair_69',
            'password_confirmation': 'Altair_6969'
        })
        self.assertFalse(form.submit())
        assert 'password_confirmation' in form.errors
