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
    return render_template('show_all.jinja', films=films)

@films_blueprint.route('films/new')
def add_new():