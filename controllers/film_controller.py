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

@films_blueprint.route("/films/delete/<id>", methods={"POST"})
def delete(id):
    film = Film.query.get(id)
    db.session.delete(film)
    db.session.commit()
    return redirect ('/films')

@films_blueprint.route('/films/edit/<id>')
def edit(id):
    film = Film.query.get(id)
    users = User.query.all()
    return render_template('films/edit.jinja', film=film, users=users)

@films_blueprint.route('/films/edit/<id>', methods=["POST"])
def update(id):
    title = request.form["title"]
    genre = request.form["genre"]
    release_date = request.form["release_date"]
    run_time = request.form["run_time"]
    user_id = request.form["user.id"]
    watched = "watched" in request.form
    film = Film.query.get(id)
    film.title = title
    film.genre = genre
    film.release_date = release_date
    film.run_time = run_time
    film.user_id = user_id
    film.watched = watched
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