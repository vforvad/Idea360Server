from . import Form, fields, validators, User

class AuthorizationForm(Form):
    """ Form for user authorization """

    email = fields.StringField('email', [validators.DataRequired(), validators.Email()])
    password = fields.PasswordField('password', [validators.DataRequired()])

    def submit():
        """ Authorize user and return token """
