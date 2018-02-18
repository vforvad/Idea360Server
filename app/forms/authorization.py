from . import BaseForm, fields, validators, User, sqlalchemy, encode_user

class AuthorizationForm(BaseForm):
    """ Form for user authorization """

    schema = {
        'email': {
            'type': 'string',
            'empty': False,
            'required': True,
            'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        },
        'password': {
            'type': 'string',
            'empty': False,
            'required': True
        }
    }

    def submit(self):
        """ Authorize user and return token """

        if not self.is_valid(): return False

        try:
            email = self.params.get('email')
            password = self.params.get('password')
            user = User.query.filter_by(email=email).one()
            if user.authenticate(password):
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
