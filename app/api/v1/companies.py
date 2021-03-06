from . import Resource, request, Company
from app.schemas import CompanySchema
from app.forms import CompanyForm
from app.services.authentication import authenticate

list_schema = CompanySchema(only=['id', 'name', 'created_at'], many=True)
single_schema = CompanySchema()

class CompaniesResource(Resource):
    """ Companies resource """

    def get(self):
        """ Receive a list of companies """

        companies = Company.query.all()
        return { 'companies': list_schema.dump(companies).data }, 200

    @authenticate
    def post(self):
        """ Creates new company """

        form = CompanyForm(obj=Company(), params=request.get_json())
        if form.submit():
            return { 'company': single_schema.dump(form.object).data }, 200
        else:
            return { 'errors': form.errors }, 400
