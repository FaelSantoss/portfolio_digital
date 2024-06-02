from flask import Blueprint, render_template

projects_views = Blueprint("projects_views", __name__)

from .personal_projects_view import personal_projects_view

@projects_views.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@projects_views.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@projects_views.route("/projects", methods=["GET"])
def projects():
    return render_template("projects/index.html")


@projects_views.route("/projects/academic", methods=["GET"])
def academic_projects():
    return render_template("projects/academic_projects.html")


@projects_views.route("/projects/personal", methods=["GET"])
def personal_projects():
    return personal_projects_view()
