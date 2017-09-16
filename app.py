from flask import Flask
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
api = Api(app)
db = SQLAlchemy(app)

from models import *

class HelllWorld(Resource):
    def get(self):
        return { 'hello': 'world' }

api.add_resource(HelllWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
