from flask import render_template
from app import app


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
