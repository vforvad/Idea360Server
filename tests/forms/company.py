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

        form = CompanyForm(obj=Company(), params={
            'name': 'Company name'
        })
        self.assertTrue(form.is_valid())

    def test_success_full_validation(self):
        """ Test success form validation with all necessary attributes """

        form = CompanyForm(obj=Company(), params={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': str(datetime.date.today())
        })
        self.assertTrue(form.is_valid())

    def test_success_form_submit(self):
        """ Test success form submit """

        form = CompanyForm(obj=Company(), params={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': str(datetime.date.today())
        })
        assert form.submit(), True

    def test_create_new_company(self):
        """ Test creating of the new company """

        companies_count = Company.query.count()
        form = CompanyForm(obj=Company(), params={
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': str(datetime.date.today())
        })
        form.is_valid()
        form.submit()
        assert Company.query.count(), companies_count + 1

    def test_failed_validation(self):
        """ Test failed company validation """

        form = CompanyForm(obj=Company(), params=None)
        self.assertFalse(form.is_valid())

    def test_failed_submit(self):
        """ Test failed company submit """

        form = CompanyForm(obj=Company(), params=None)
        self.assertFalse(form.submit())

    def test_success_company_update(self):
        """ Test success company updating action """
        
        params = {
            'name': 'Teeest',
            'description': 'description',
            'city': 'City',
            'start_date': str(datetime.date.today())
        }

        form = CompanyForm(obj=self.company, params=params)
        form.submit()
        assert form.obj.name, params.get('name')
