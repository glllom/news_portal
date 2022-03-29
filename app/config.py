import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '40cdft9aea1W3FQ1@5e8Ff!481$f4O76'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'Users.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
