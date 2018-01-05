from . import (
    Form, fields, validators, db,
    Company, sqlalchemy
)
import ipdb

class CompanyForm(Form):
    """ Form object for creating the company """

    name = fields.StringField('name', [validators.DataRequired()])
    description = fields.StringField('description')
    start_date = fields.DateField('start_date', format='%d-%m-%Y')
    city = fields.StringField('city')

    def __init__(self, obj, *args, **kwargs):
        self.obj = obj
        super(CompanyForm, self).__init__(*args, **kwargs)

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
            company = self.obj
        else:
            company = Company(**params)
            db.session.add(company)
        db.session.commit()
        self.object = company
        return True
