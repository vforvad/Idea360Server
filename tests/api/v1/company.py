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
            'start_date': str(datetime.datetime.now())
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

    def test_succes_company_update(self):
        """ Updates existing company """

        res = self.client().put(
            '/api/v1/companies/{}'.format(self.company.id),
            data=json.dumps(self.params),
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert res.status_code, 200

    def test_updating_of_the_company(self):
        """ Check changing of the company attributes """

        res = self.client().put(
            '/api/v1/companies/{}'.format(self.company.id),
            data=json.dumps(self.params),
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert self.company.name, self.params['name']

    def test_failed_updating_of_the_company(self):
        """ Test failed company update """

        res = self.client().put(
            '/api/v1/companies/{}'.format(self.company.id),
            data=json.dumps(None),
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert res.status_code, 400

    def test_success_company_delete(self):
        """ Test success company deletion """

        res = self.client().delete(
            '/api/v1/companies/{}'.format(self.company.id),
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert res.status_code, 204
