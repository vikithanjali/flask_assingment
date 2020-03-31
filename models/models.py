from flask_sqlalchemy import SQLAlchemy
from app import db
# db = SQLAlchemy()

class Users(db.Model):
    """user model"""
    __tablename__ ="users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)
    salary = db.Column(db.Integer)


class Loan(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    loan_request_date = db.Column(db.Date)

db.create_all()