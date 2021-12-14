import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('routes', __name__)


# before each request it checks if the user is logged in, and if they are, it saves it to g.user, as well as all the other user information. 
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


# handles the login. A successful login redirects the user to the home page. 
@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        form = request.form.to_dict()
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (form["username"],)
        ).fetchone()
        if user is None:
            flash("Error: user does not exist.")
        elif not check_password_hash(user["password"], form["password"]):
            flash("Error: password incorrect for user.")
        else:
            session["user_id"] = user["id"]
            return redirect(url_for("website.home"))

    return render_template("login.html")


# home webpage. Contains the vigenere cipher text and hidden key. 
@bp.route("/home", methods=("GET",))
def home():
    return render_template("home.html")


# checks if a username exists. Has an intentional sql error.
@bp.route("/does-my-username-exist", methods=("GET", "POST"))
def check_username():
    if request.method == "POST":
        form = request.form.to_dict()
        db = get_db()
        user = db.execute(
            'SELECT username FROM user WHERE username = "{}"'.format(form["username"])
        ).fetchone()
        # user = dict(user)
        if user:
            user = dict(zip(user.keys(), user)) 
            print(user)
            flash(", ".join("The {} {} exists".format(key, value) for key, value in user.items()))
        else:
            flash("username does not exist.")

    return render_template("check username.html")


# adds a user to the database. 
@bp.route("/add-user", methods=("GET", "POST"))
def add_user():
    if request.method == "POST":
        form = request.form.to_dict()
        db = get_db()
        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (form["username"], generate_password_hash(form["password"]))
        )

        db.commit()

        flash("User successfully added.")
    
    return render_template("add user.html")
