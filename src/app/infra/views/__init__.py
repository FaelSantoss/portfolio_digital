from flask import Flask
from .project_views import projects_views


def init_views(app: Flask):
    app.register_blueprint(projects_views)
