from turtle import title
from app import db


class User_data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    location = db.Column(db.String(50))
    language = db.Column(db.String(50))
