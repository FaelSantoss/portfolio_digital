from flask import Blueprint, render_template, request

projects_views = Blueprint("projects_views", __name__)

from .projects_view import projects_view
from .home_projects_view import home_projects_view


@projects_views.route("/", methods=["GET"])
def homepage():
    url = str(request.path)
    return render_template("index.html", url=url)


@projects_views.route("/about", methods=["GET"])
def about():
    url = str(request.path)
    return render_template("about.html", url=url)


@projects_views.route("/projects", methods=["GET"])
def projects():
    return home_projects_view()

@projects_views.route("/projects/<title>", methods=["GET"])
def personal_projects(title):
    return projects_view()
