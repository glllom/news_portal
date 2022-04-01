from app import db


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(35), unique=True, index=True)
    password = db.Column(db.String(16))
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    language = db.Column(db.String(50))
    last_search = db.Column(db.String(50))
    userstocks = db.relationship('User_Stocks', backref='user_data', lazy='dynamic')

    def set_firstname(self, firstname):
        self.firstname = firstname
        db.session.commit()

    def set_lastname(self, lastname):
        self.lastname = lastname
        db.session.commit()

    def set_country(self, country):
        self.country = country
        db.session.commit()

    def set_city(self, city):
        self.city = city
        db.session.commit()

    def set_language(self, language):
        self.language = language
        db.session.commit()

    def set_search_word(self, word):
        self.last_search = word
        db.session.commit()

    def get_search_word(self):
        return self.last_search

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

class User_Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String(25))
    stock_name = db.Column(db.String(25))
    opening = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    previous_close = db.Column(db.Float)
    closing = db.Column(db.Float)
    change = db.Column(db.Float)
    perc = db.Column(db.String(15))
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.id'))