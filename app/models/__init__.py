from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

from .user import User
from .company import Company
