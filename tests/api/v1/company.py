from . import (
    BaseTestCase, json, UserFactory,
    Company, CompanyFactory, encode_user, AUTH_HEADER
)
import datetime
import ipdb

class CompanyViewTest(BaseTestCase):
    """ Company View tests """

    def setUp(self):
        """ Setting up test deepndencies """

        self.user = UserFactory.create()
        self.company = CompanyFactory.create()
        self.db.session.add(self.user)
        self.db.session.add(self.company)
        self.db.session.commit()
        self.token = encode_user(self.user)
        self.params = {
            'name': 'Company name',
            'description': 'description',
            'city': 'City',
            'start_date': datetime.datetime.now()
        }

    def test_success_company_receiving(self):
        """ Test success receiving of the companies list """

        res = self.client().get(
            '/api/v1/companies/{}/'.format(self.company.id),
            content_type='application/json'
        )
        assert res.status_code, 200

    def test_success_company_attributes(self):
        """ Test correct company attributes """

        res = self.client().get(
            '/api/v1/companies/{}/'.format(self.company.id),
            content_type='application/json'
        )

        for attribute in ['id', 'name', 'description']:
            assert getattr(self.company, attribute), res.data['companies'][attribute]
