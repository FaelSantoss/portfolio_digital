from core.entities.projects import Projects
from core.commons import Error
from infra.database import mysql

class ProjectsRepository:
    def get_projects(self) -> list[Projects]:
        select_query = "SELECT * FROM projects"
        rows = mysql.query(sql=select_query, is_single=False)

        projects = []

        for row in rows:
            projects.append(self.__get_project_entity(row))

        return projects
    
    def get_projects_by_title(self, title) -> Projects | None:
        row = mysql.query(
            sql="SELECT * FROM projects WHERE title = %s",
            params=[title]
        )

        if row:
            return self.__get_project_entity(row)
        
        return None

    def get_icons_by_technologies(self, technologies):
        try:
            technologies_icons = []
            for technologie in technologies:
                    technologies_icons.append(f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{technologie}/{technologie}-original.svg")
        except Error as error:
            raise error
        
        return technologies_icons
        
    def __get_project_entity(self,row):
        return Projects(id=row["id"], title=row["title"], content=row["content"], technologies=row["technologies"], link=row["link"], img=row["img"])