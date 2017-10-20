from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
import yaml
import ipdb

from config import app_config
from app.api import api_v1_bp
from app.models import db
from app.schemas import ma

def create_app(config_name):
    """ Basic application creation """
    app = Flask(__name__)
    
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app
