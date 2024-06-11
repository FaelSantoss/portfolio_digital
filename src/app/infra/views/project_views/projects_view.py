from flask import render_template, request

from infra.repositories import projects_repository


def projects_view():
    url = str(request.path)
    title = url.replace('/projects/', '')
    project = projects_repository.get_projects_by_title(title)
    technologies_icons = projects_repository.get_icons_by_technologies(project.technologies.split(','))

    return render_template(
        "projects/projects.html", project=project, url=url, title=title, technologies_icons=technologies_icons
    )
