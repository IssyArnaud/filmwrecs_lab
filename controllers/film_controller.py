from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.user import User
from models.film import Film
from app import db

films_blueprint = Blueprint("films", __name__)

@films_blueprint.route("/home")
def index():
    return render_template("index.jinja", title="filmwrecs")

@films_blueprint.route('/films')
def show_all():
    films = Film.query.all()
    return render_template('films/show_all.jinja', films=films)

@films_blueprint.route("/films/watched/<id>", methods=["POST"])
def watched(id):
    film = Film.query.get(id)
    film.watched = True
    db.session.commit()
    return redirect ('/films')

@films_blueprint.route('/films/new')
def new():
    users = User.query.all()
    return render_template('films/new.jinja', users=users)

@films_blueprint.route('/films/new', methods=["POST"])
def add_new():
    title = request.form["title"]
    genre = request.form["genre"]
    release_date = request.form["release_date"]
    run_time = request.form["run_time"]
    user_id = request.form["user.id"]
    new_film = Film(title=title, genre=genre, release_date=release_date, run_time=run_time, user_id=user_id)

    db.session.add(new_film)
    db.session.commit()
    return redirect ('/films')