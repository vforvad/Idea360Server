from . import BaseTestCase, CompanyFactory
from app.forms.company import CompanyForm

class CompanyFormTest(BaseTestCase):
    """ CompanyForm tests """

    def success_validation(self):
        """ Test success form validation """

        form = CompanyForm(data={
            'name': 'Company name'
        })
        self.assertTrue(form.validate())
