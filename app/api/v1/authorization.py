from . import Resource, request
from app.forms import AuthorizationForm

class AuthorizationResource(Resource):
    """ Authorization Resource """

    def post(self):
        """ Authorize user via its credentials """

        form = AuthorizationForm(data=request.get_json())
        if form.submit():
            return { 'token': str(form.token) }, 200
        else:
            return { 'errors': form.errors }, 400
