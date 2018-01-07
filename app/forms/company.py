from . import (
    Form, fields, validators, db,
    Company, CompanyUser, sqlalchemy
)
from flask import g
import ipdb

class CompanyForm(Form):
    """ Form object for creating the company """

    DEFAULT_ROLE = 0

    name = fields.StringField('name', [validators.DataRequired()])
    description = fields.StringField('description')
    start_date = fields.DateField('start_date', format='%d-%m-%Y')
    city = fields.StringField('city')

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.get('obj', None)
        super(CompanyForm, self).__init__(*args, **kwargs)

    def validate(self):
        """ Override of the validation """

        try:
            valid = Form.validate(self)
            if not valid:
                return False
            self.current_user = g.current_user
            return True
        except AttributeError as e:
            self.errors['current_user'] = ['Current user is not present']
            return False

    def submit(self):
        """ Create new company instance """

        if not self.validate(): return False

        params = {
            'name': self.name.data,
            'description': self.description.data,
            'start_date': self.start_date.data,
            'city': self.city.data
        }
        if self.obj:
            db.session.query(Company).filter_by(
                id=self.obj.id).update(values=params)
        else:
            company = Company(**params)
            company_user = CompanyUser(
                role=self.DEFAULT_ROLE
            )
            company.employees.append(company_user)
            self.current_user.companies.append(company_user)
            db.session.add(company)
        db.session.commit()
        self.object = company
        return True


    def __create_company(params):
        """ Create new company """

        company = Company(**params)
        company_user = CompanyUser(
            user_id=g.current_user.id,
            company_id=company.id,
            role=self.DEFAULT_ROLE
        )
        db.session.add(company)
        db.session.add(company_user)

    def __update_company(params):
        """ Update company information """

        db.session.query(Company).filter_by(
            id=self.obj.id).update(values=params)
