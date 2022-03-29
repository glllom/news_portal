from __future__ import unicode_literals

from app import db


class UserData(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(35), unique=True, index=True)
    password = db.Column(db.String(16))
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    language = db.Column(db.String(50))
    last_search = db.Column(db.String(50))

    def set_search_word(self, word):
        self.last_search = word
        db.session.commit()

    def get_search_word(self):
        return self.last_search

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country
