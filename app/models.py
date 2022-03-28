from __future__ import unicode_literals
from turtle import title
from app import db
from flask_login import  UserMixin

class User_data(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(35), unique=True)
    password = db.Column(db.String(16))
    location = db.Column(db.String(50))
    language = db.Column(db.String(50))
