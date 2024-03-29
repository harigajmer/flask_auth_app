from . import db
from flask_login import UserMixin
from project import db, create_app

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))




db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.