import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('routes', __name__)


# credit: the following function (login_required) is from the flask tutorial and slightly altered.

# disallows access to pages unless the user is logged in.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not "user_id" in session:
            return redirect(url_for('routes.login'))

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
            session.clear()
            session["user_id"] = user["id"]
            # these two values are not included in the session because that causes the session to compress, which adds needless
            # complexity for the students completing the cookie stealing challenge. 
            # session["username"] = user["username"]
            # session["password"] = form["password"]
            # the adm password is qwe123
            return redirect(url_for("routes.home"))

    return render_template("login.html")


# home webpage. Contains the vigenere cipher text and hidden key. The user is required to be logged in before accessing it. 
@bp.route("/home", methods=("GET",))
@login_required
def home():
    if session["user_id"] == 6:
        session["vigenere cipher"] = "zwyyg://eas.drmwzks.ksi/bdlfm?e=rYa4s9BjPfV"
        # session["important"] = "The key is hidden in the home page"
        session["nb"] = "The key is hidden in the home page"
        return render_template("home.html")
    else:
        return redirect(url_for('routes.login'))


# checks if a username exists. Has an intentional sql error.
@bp.route("/does-my-username-exist", methods=("GET", "POST"))
def check_username():
    if request.method == "POST":
        form = request.form.to_dict()
        db = get_db()
        print("SELECT username FROM user WHERE username = '{}'".format(form["username"]))
        user = db.executescript(
            "SELECT username FROM user WHERE username = '{}'".format(form["username"])
        ).fetchone()
        # user = dict(user)
        if user:
            flash("The username {} exists".format(user["username"]))
        else:
            flash("The username {} does not exist".format(form["username"]))

    return render_template("check username.html")


# adds a user to the database. 
@bp.route("/add-user", methods=("GET", "POST"))
def add_user():
    if request.method == "POST":
        form = request.form.to_dict()
        db = get_db()

        # I didn't put a unique constraint on the username, because I thought perhaps there could be 
        # some sort of exploit using that. Such as adding a user with the username adm and password 123 and logging in as that user.
        # however /login is written to fetch the first instance of an account with the username adm, which is the original password
        # I selected from the rockyou list. 

        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (form["username"], generate_password_hash(form["password"]))
        )

        db.commit()

        flash("User successfully added.")

        return redirect(url_for("routes.login"))
    
    return render_template("add user.html")

# clears the session for testing purposes. Will be deleted before finalizing the project. 
@bp.route("/clear-session", methods=("GET",))
def clear_session():
    session.clear()
    return redirect(url_for("routes.login"))