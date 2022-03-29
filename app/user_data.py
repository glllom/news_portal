from app import db
from app.models import UserData


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
    UserData.query.get(user.user_id).set_search_word(word)


def get_word(user):
    return UserData.query.get(user.user_id).get_search_word()

def delete_user(email):
    to_delete = UserData.query.filter_by(email=email).first()
    db.session.delete(to_delete)
    db.session.commit()