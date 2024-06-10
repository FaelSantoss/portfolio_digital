from flask import render_template, request

from infra.repositories import personal_projects_repository


def personal_projects_view():
    url = str(request.path)
    title = url.replace('/projects/personal/', '')
    personal_project = personal_projects_repository.get_personal_projects_by_title(title)
    technologies_icons = personal_projects_repository.get_icons_by_technologies(personal_project.technologies.split(','))
    print(technologies_icons, flush=True)
    return render_template(
        "projects/personal_projects.html", personal_project=personal_project, url=url, title=title, technologies_icons=technologies_icons
    )
