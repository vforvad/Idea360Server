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

    companies = db.relationship('CompanyUser', backref=db.backref('users', lazy=True))

    def __init__(self, **kwargs):
        password = kwargs.pop('password', None)
        super(User, self).__init__(**kwargs)
        self.password_digest = self.set_password(password)

    def set_password(self, password):
        """ Hash and store password """

        return bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()
        ).decode('utf8')

    def authenticate(self, password):
        """ Authenticate user; Check if user's password match the given one """

        return bcrypt.checkpw(password.encode(), self.password_digest.encode())
