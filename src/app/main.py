from flask import Blueprint, Flask, render_template, request

# Projects data
projects_data = [
    {
        "title": "Smart-Farming",
        "content": "Desenvolvemos uma aplicação web para o monitoramento remoto e análise de dados de uma estufa na faculdade. Minhas contribuições incluíram o desenvolvimento do backend, criação de repositórios (CRUD), entidades, exportação de dados para .xlsx e participação significativa na modelagem do banco de dados.",
        "technologies": "javascript,python,flask,html5,css3,tailwindcss,docker,mysql",
        "link": "https://github.com/CtrI-Alt-Del/smart-farming",
        "img": "smartfarming.png",
    },
    {
        "title": "Meu-Timao",
        "content": "Desenvolvi o site 'Meu Timao', onde os usuários podem adicionar notícias que são exibidas em forma de cards. Cada card possui um botão que gera uma rota dinâmica para uma página específica no banco de dados. A interface inclui um carrossel com as três últimas notícias, utilizando componentes do Bootstrap.",
        "technologies": "python,flask,html5,css3,bootstrap,docker,mysql",
        "link": "https://github.com/FaelSantoss/meu-timao",
        "img": "meutimao.png",
    },
    {
        "title": "Todo-List",
        "content": "Desenvolvi o 'Todo Avançado', uma aplicação para adicionar, pesquisar, filtrar, editar e excluir tarefas.",
        "technologies": "javascript,html5,css3",
        "link": "https://github.com/FaelSantoss/projeto-todo",
        "img": "todolist.png",
    },
    {
        "title": "Buscador-CEP",
        "content": "Desenvolvi o 'Buscador CEP', uma aplicação que utiliza uma API externa para buscar informações de endereço com base no CEP inserido pelo usuário.",
        "technologies": "javascript,react,html5,css3",
        "link": "https://github.com/FaelSantoss/zip-code-finder",
        "img": "zipcodefinder.png",
    },
]


# Repository class
class ProjectsRepository:
    def get_projects_by_title(self, title, data):
        for project in data:
            if project["title"] == title:
                return project
        return None

    def get_icons_by_technologies(self, technologies):
        try:
            technologies_icons = []
            for technology in technologies:
                technologies_icons.append(
                    f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{technology}/{technology}-original.svg"
                )
            return technologies_icons
        except:
            return None


projects_repository = ProjectsRepository()


# View functions
def projects_view():
    url = str(request.path)
    title = url.replace("/projects/", "")
    project = projects_repository.get_projects_by_title(title, projects_data)
    technologies_icons = projects_repository.get_icons_by_technologies(
        project["technologies"].split(",")
    )
    return render_template(
        "projects/projects.html",
        project=project,
        url=url,
        title=title,
        technologies_icons=technologies_icons,
    )


def home_projects_view():
    url = str(request.path)
    return render_template(
        "projects/index.html",
        projects=projects_data,
        url=url,
    )


# Blueprint
projects_views = Blueprint("projects_views", __name__)


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


# App initialization
def init_views(app: Flask):
    app.register_blueprint(projects_views)


def create_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )
    app.config["SECRET_KEY"] = "1234"
    app.config["UPLOAD_FOLDER"] = "static/uploads"
    init_views(app)
    return app


# Main entry point
app = create_app()
