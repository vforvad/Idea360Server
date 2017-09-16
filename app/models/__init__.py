from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User
