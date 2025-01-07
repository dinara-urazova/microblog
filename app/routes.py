from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Dinara"}
    posts = [
        {
            "author": {"username": "Patrick"},
            "body": "Beautiful day in Paris!"
        },

        {
            "author": {"username": "David"},
            "body": "The Dreamers mode is on!"
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # False if Get-request, True if Post-request (user presses the submit button)
        flash(f"Login requested for user {form.username.data}, remember_me = {form.remember_me.data}")
        return redirect("/index")
    
    return render_template("login.html", title="Sign In", form=form)