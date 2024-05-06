from flask import render_template
from portifolio import app


@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html")
