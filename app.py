from flask import Flask
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
import os
import yaml

app = Flask(__name__)

if os.path.isfile('secrets.yaml'):
    with open('secrets.yaml') as stream:
        f = yaml.load(stream)
        for k, v in f.items():
            os.environ[k] = v


app.config.from_object(os.environ['APP_SETTINGS'])
api = Api(app)
db = SQLAlchemy(app)

from models import *

class HelllWorld(Resource):
    def get(self):
        return { 'hello': 'world' }

api.add_resource(HelllWorld, '/')
