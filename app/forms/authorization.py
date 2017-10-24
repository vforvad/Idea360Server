from . import Form, fields, validators, User, sqlalchemy, encode_user

class AuthorizationForm(Form):
    """ Form for user authorization """

    email = fields.StringField('email', [validators.DataRequired(), validators.Email()])
    password = fields.PasswordField('password', [validators.DataRequired()])

    def submit():
        """ Authorize user and return token """

        if not self.validate(): return False

        try:
            user = User.query.filter_by(email=self.email.data).one()
            if user.authenticate(self.password.data):
                self.token = encode_user(user)
                return True
            else:
                raise sqlalchemy.orm.exc.NoResultFound()

        except sqlalchemy.orm.exc.NoResultFound:
            return self._error_message('There is no such user')

    def _error_message(self, message):
        """ Set error message and return negative result """

        self.errors['user'] = [message]
        return False
