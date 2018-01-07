from . import db, datetime

company_users = db.Table('company_users',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True, nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False),
    db.Column('role', db.Integer, index=True),
    db.Column('created_at', db.DateTime(), default=datetime.datetime.now),
    db.Column('updated_at', db.DateTime(), onupdate=datetime.datetime.now)
)
