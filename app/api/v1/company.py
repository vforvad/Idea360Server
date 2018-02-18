from . import Resource, request, Company
from app.schemas import CompanySchema
from app.forms import CompanyForm
from app.services.authentication import authenticate
from app.utils import get_object_or_404

single_schema = CompanySchema()

class CompanyResource(Resource):
    """ Company resource """

    def get(self, company_id):
        """ Receive a detail company information """

        company = get_object_or_404(Company, company_id)
        return { 'company': single.dump(company).data }, 200

    @authenticate
    def put(self, company_id):
        """ Update existing company """

        company = get_object_or_404(Company, company_id)
        form = CompanyForm(obj=company, data=request.get_json())
        if form.submit():
            return { 'company': single_schema.dump(company).data }, 200
        else:
            return { 'errors': form.errors }, 400

    @authenticate
    def delete(self, company_id):
        """ Delete existing company """

        company = Company.query.filter_by(id=company_id)
        company.delete()
        return { }, 204
