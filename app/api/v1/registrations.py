from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse
from app.forms import RegistrationForm
import ipdb

class RegistrationsResource(Resource):
    """ Registration resource """

    def post(self):
        """ receive user params and create a new user """

        form = RegistrationForm(data=request.get_json())
        if form.submit():
            return { 'token': str(form.token) }, 201
        else:
            # ipdb.set_trace()
            return { 'errors', str(form.errors) }, 400
