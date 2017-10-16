from wtforms import Form, fields, validators

from app.models import db, User

class RegistrationForm(Form):
    email = fields.StringField('email', [validators.Email()])
    password = fields.PasswordField('password', [validators.InputRequired()])
    password_confirmation = fields.PasswordField('password_confirmation', [
        validators.InputRequired(),
        validators.EqualTo('password', message='Does\'t match password')
    ])


    def submit(self):
        """ Perform registration """

        if not self.validate(): return False
        try:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            self.object = user
            return True
        except:
            return False
