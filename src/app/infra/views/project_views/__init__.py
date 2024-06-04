from flask import Blueprint, render_template, request

projects_views = Blueprint("projects_views", __name__)

from .personal_projects_view import personal_projects_view


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
    url = str(request.path)
    return render_template("projects/index.html", url=url)


@projects_views.route("/projects/academic", methods=["GET"])
def academic_projects():
    return render_template("projects/academic_projects.html")


@projects_views.route("/projects/personal", methods=["GET"])
def personal_projects():
    return personal_projects_view()
