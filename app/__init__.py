from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
import yaml

from app.api import api_v1_bp
from app.models import db
from app.schemas import ma


def load_secrets():
    if os.path.isfile('secrets.yaml'):
        with open('secrets.yaml') as stream:
            f = yaml.load(stream)
            for k, v in f.items():
                os.environ[k] = v

def create_app():
    """ Basic application creation """
    load_secrets()
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app
