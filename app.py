from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/blockbuster"
db = SQLAlchemy(app)

from models.user import User
from models.film import Film

migrate = Migrate(app, db)

from controllers.film_controller import films_blueprint
app.register_blueprint(films_blueprint)