from flask import render_template
from portfolio import app


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects/index.html")

@app.route("/projects/academic", methods=["GET"])
def academic_projects():
    return render_template("projects/academic_projects.html")

@app.route("/projects/personal", methods=["GET"])
def personal_projects():
    return render_template("projects/personal_projects.html")