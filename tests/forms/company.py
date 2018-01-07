from . import BaseTestCase, UserFactory, CompanyFactory, g
from app.forms.company import CompanyForm
from app.models import Company
import datetime
import ipdb

class CompanyFormTest(BaseTestCase):
    """ CompanyForm tests """

    def setUp(self):
        """ Setting up test dependencies """

        self.user = UserFactory()
        self.company = CompanyFactory()
        g.current_user = self.user

    def test_success_validation(self):
        """ Test success form validation """

        form = CompanyForm(data={
            'name': 'Company name'
        })
        self.assertTrue(form.validate())

    def test_success_full_validation(self):
        """ Test success form validation with all necessary attributes """

        form = CompanyForm(data={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': datetime.datetime.now()
        })
        self.assertTrue(form.validate())

    def test_success_form_submit(self):
        """ Test success form submit """

        form = CompanyForm(data={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': datetime.datetime.now()
        })
        assert form.submit(), True

    def test_create_new_company(self):
        """ Test creating of the new company """

        companies_count = Company.query.count()
        form = CompanyForm(data={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': datetime.datetime.now()
        })
        form.validate()
        form.submit()
        assert Company.query.count(), companies_count + 1

    def test_failed_validation(self):
        """ Test failed company validation """

        form = CompanyForm(data=None)
        self.assertFalse(form.validate())

    def test_failed_submit(self):
        """ Test failed company submit """

        form = CompanyForm(data=None)
        self.assertFalse(form.validate())
