from . import (
    BaseForm, fields, validators, db,
    Company, CompanyUser, sqlalchemy
)
from flask import g
import ipdb

class CompanyForm(BaseForm):
    """ Form object for creating the company """

    schema = {
        'name': {
            'type': 'string',
            'empty': False,
            'required': True
        },
        'description': {
            'type': 'string',
            'empty': True,
            'required': False
        },
        'start_date': {
            'type': 'string',
            'regex': '^\d{4}-\d{2}-\d{2}$',
            'empty': True,
            'required': False
        },
        'city': {
            'type': 'string',
            'empty': True,
            'required': False
        }
    }

    DEFAULT_ROLE = 0

    @property
    def current_user(self):
        """ Current user object """

        return g.current_user

    def submit(self):
        """ Create new company instance """

        if not self.is_valid(): return False

        params = {
            'name': self.params.get('name'),
            'description': self.params.get('description'),
            'start_date': self.params.get('start_date'),
            'city': self.params.get('city')
        }
        self._set_attributes_for_company()
        if not self.obj.id:
            self._create_company_member()
        db.session.add(self.obj)
        db.session.commit()
        return True

    def _set_attributes_for_company(self):
        """ Set form attributes to the company instance """

        for field, value in self.params.items():
            setattr(self.obj, field, value)

    def _create_company_member(self):
        """ Create company member relation between company and user """

        company_user = CompanyUser(
            role=self.DEFAULT_ROLE
        )
        self.obj.employees.append(company_user)
        self.current_user.companies.append(company_user)
