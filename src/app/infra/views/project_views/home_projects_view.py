from flask import render_template, request

from infra.repositories import projects_repository


def home_projects_view():
    url = str(request.path)
    projects = projects_repository.get_projects()
    projects_url = []
    for project in projects:
        projects_url.append(url + '/' + project.title)

    return render_template(
        "projects/index.html", projects=projects, url=url, projects_url=projects_url
    )
