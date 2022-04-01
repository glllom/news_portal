from app import db
from app.models import User_Stocks, UserData


def add_user(firstname, lastname, email, country, city, language, password):
    new_user = UserData(firstname=firstname, lastname=lastname,
                        email=email, country=country, city=city, language=language, password=password)

    db.session.add(new_user)
    db.session.commit()


def check_user(email):
    return UserData.query.filter_by(email=email).first()


def check_password(email, password):
    return password == UserData.query.filter_by(email=email).first().password


def set_word(user, word):
    UserData.query.get(user.id).set_search_word(word)


def get_word(user):
    return UserData.query.get(user.id).get_search_word()


def update_user(user, firstname, lastname, country, city, language):
    user = UserData.query.get(user.id)
    user.set_firstname(firstname)
    user.set_lastname(lastname)
    user.set_country(country)
    user.set_city(city)
    user.set_language(language)


""" -------------------------------USER STOCKS------------------------------- """
def add_stock(stock_symbol, stock_name, date, opening, high, low, previous_close, closing, change, perc, user_id):
                
    new_stock = User_Stocks(stock_symbol=stock_symbol, stock_name=stock_name, date=date, opening=opening, high=high, low=low, previous_close=previous_close, closing=closing, change=change, perc=perc, user_id=user_id)
    
    
    db.session.add(new_stock)
    db.session.commit()

def remove_stock(stock):
    db.session.delete(stock)
    db.session.commit()

def user_stocks(id):
    return db.session.query(User_Stocks).filter(User_Stocks.user_id == id)