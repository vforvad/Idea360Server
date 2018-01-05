from . import SQLAlchemyModelFactory, db, fake
import datetime
from app.models import Company

class CompanyFactory(SQLAlchemyModelFactory):
    """ Factory for the company model """

    class Meta:
        model = Company
        sqlalchemy_session = db.session

    name = fake.name
    description = fake.text()
    start_date = datetime.datetime.now()
    city = fake.address()
