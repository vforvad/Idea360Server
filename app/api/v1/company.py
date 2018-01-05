from . import Resource, request, Company
from app.schemas import CompanySchema
from app.forms import CompanyForm
from app.services.authentication import authenticate

single_schema = CompanySchema()

class CompanyResource(Resource):
    """ Company resource """

    def get(self, company_id):
        """ Receive a detail company information """

        company = Company.query.get(company_id)
        return { 'company': single.dump(company).data }, 200

    def put(self, company_id):
        """ Update existing company """

        company = Company.query.get(company_id)
        form = CompanyForm(obj=company, data=response.get_json())
        if form.submit():
            return { 'company': single.dump(company).data }, 200
        else:
            return { 'errors': form.errors }, 400
