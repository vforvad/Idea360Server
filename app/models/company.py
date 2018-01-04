from . import db
import datetime

class Company(db.Model):
    """ Company representation in the system """

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, index=True)
    description = db.Column(db.Text())
    start_date = db.Column(db.Date(), index=True)
    city = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)

    def __init__(self, name, description=None, start_date=None, city=None):
        """ Model constructor """

        self.name = na,e
        self.description = description
        self.start_date = start_date
        self.city = city
