from . import Resource, request, g, User
from app.services.authentication import authenticate

class CurrentUserResource(Resource):
    """ Current User resource """

    method_decorators = [authenticate]

    def get(self):
        return { 'current_user': g.current_user.id }
