from flask import render_template, request

from core.data import projects_data

def home_projects_view():
    url = str(request.path)

    return render_template(
        "projects/index.html", projects=projects_data, url=url,)
