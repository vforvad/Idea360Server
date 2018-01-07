from . import db, datetime

class CompanyUser(db.Model):
    """ Association object class for company and user"""

    __tablename__ = 'company_users'

    company_id = db.Column(
        db.Integer, db.ForeignKey('companies.id'), primary_key=True, nullable=False
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False
    )
    role = db.Column(db.Integer, index=True)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
