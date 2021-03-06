from . import ma

class UserSchema(ma.Schema):
    """ User JSON schema """

    class Meta:
        fields = [
            'id',
            'email',
            'first_name',
            'last_name'
        ]

user_schema = UserSchema()
users_schema = UserSchema(many=True)
