from . import SQLAlchemyModelFactory, db
from app.models import User

class UserFactory(SQLAlchemyModelFactory):
    """ Factory for user model """

    class Meta:
        model = User
        sqlalchemy_session = db.session

    email = 'example@mail.com'
    first_name = 'First Name'
    last_name = 'Last name'
