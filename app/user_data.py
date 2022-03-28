from app import db
from app.models import UserData


def add_user(firstname, lastname, email, location, language, password):
    new_user = UserData(firstname=firstname, lastname=lastname,
                        email=email, location=location, language=language, password=password)
    db.session.add(new_user)
    db.session.commit()


def check_user(email):
    return UserData.query.filter_by(email=email)


def check_password(username, password):
    pass

