from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


app = Flask(__name__, static_folder="static")

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, error_handlers, models
db.create_all()
