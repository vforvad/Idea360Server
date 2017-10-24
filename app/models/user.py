from . import db

import bcrypt

class User(db.Model):
    """ User representation in the system """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    password_digest = db.Column(db.String(), nullable=False)

    def __init__(self, email, password, first_name=None, last_name=None):
        self.email = email
        self.password_digest = self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name

    def set_password(self, password):
        """ Hash and store password """

        return bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()
        ).decode('utf8')

    def authenticate(self, password):
        """ Authenticate user; Check if user's password match the given one """

        return bcrypt.checkpw(password.encode(), self.password_digest.encode())
