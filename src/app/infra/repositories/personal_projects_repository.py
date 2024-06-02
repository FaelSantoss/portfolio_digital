from core.entities.projects import Projects
from infra.database import mysql

class PersonalProjectsRepository:
    def get_personal_projects(self) -> list[Projects]:
        select_query = "SELECT * FROM personal_project"
        rows = mysql.query(sql=select_query, is_single=False)

        personal_projects = []

        for row in rows:
            personal_projects.append(Projects(id=row["id"], title=row["title"], content=row["content"], technologies=row["technologies"], link=row["link"]))

        return personal_projects
    