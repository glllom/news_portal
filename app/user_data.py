from app import db
from app.models import UserData


def add_user(firstname, lastname, email, location, language, password):
    new_user = UserData(firstname=firstname, lastname=lastname,
                        email=email, location=location, language=language, password=password)

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
