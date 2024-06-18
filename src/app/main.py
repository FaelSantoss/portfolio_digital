from flask import Flask

from infra.views import init_views


def create_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = "1234"
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    init_views(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)