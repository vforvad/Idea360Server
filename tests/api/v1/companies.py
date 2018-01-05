from . import (
    BaseTestCase, json, UserFactory,
    Company, CompanyFactory, encode_user, AUTH_HEADER
)
import datetime
import ipdb

class CompaniesViewTest(BaseTestCase):
    """ Companies View tests """

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

    def test_success_companies_list_receiving(self):
        """ Test success receiving of the companies list """

        res = self.client().get(
            '/api/v1/companies', content_type='application/json'
        )
        assert res.status_code, 200

    def test_success_companies_list_attributes(self):
        """ Test correct companies list attributes """

        res = self.client().get(
            '/api/v1/companies', content_type='application/json'
        )

        for attribute in ['id', 'name']:
            assert getattr(self.company, attribute), res.data['companies'][attribute]

    def test_failed_company_creation_without_auth_token(self):
        """ Test failed creation of the company without auth token """

        res = self.client().post(
            '/api/v1/companies',
            data=self.params,
            content_type='application/json'
        )
        assert res.status_code, 401

    def test_success_company_creation(self):
        """ Test correct company creaion """

        res = self.client().post(
            '/api/v1/companies',
            data=self.params,
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert res.status_code, 200

    def test_changing_companies_number(self):
        """ Test changing number of the companies """

        companies_count = Company.query.count()
        res = self.client().post(
            '/api/v1/companies',
            data=self.params,
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert Company.query.count(), companies_count + 1

    def test_failed_company_creation(self):
        """ Test failed company creation """

        res = self.client().post(
            '/api/v1/companies',
            data=None,
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        assert res.status_code, 400

    def test_failed_company_creation_errors(self):
        """ Test receiving errors from company creation """

        res = self.client().post(
            '/api/v1/companies',
            data=json.dumps(None),
            content_type='application/json',
            headers={AUTH_HEADER: self.token}
        )
        response_data = json.loads(res.data)
        self.assertTrue('errors' in response_data)
