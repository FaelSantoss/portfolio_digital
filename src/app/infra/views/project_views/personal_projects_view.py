from flask import render_template, request

from infra.repositories import personal_projects_repository


def personal_projects_view():
    url = str(request.path)
    personal_projects = personal_projects_repository.get_personal_projects()
    return render_template(
        "projects/personal_projects.html", personal_projects=personal_projects, url=url
    )
