from . import db

class User(db.Model):
    """ User representation in the system """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    password_digest = db.Column(db.String())

    def __init__(self, email, password=None, first_name=None, last_name=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
