from core.entities.projects import Projects
from infra.database import mysql

class PersonalProjectsRepository:
    def get_personal_projects(self) -> list[Projects]:
        select_query = "SELECT * FROM personal_project"
        rows = mysql.query(sql=select_query, is_single=False)

        personal_projects = []

        for row in rows:
            personal_projects.append(self.__get_project_entity(row))

        return personal_projects
    
    def get_personal_projects_by_title(self, title) -> Projects | None:
        row = mysql.query(
            sql="SELECT * FROM personal_project WHERE title = %s",
            params=[title]
        )

        if row:
            return self.__get_project_entity(row)
        
        return None
        
    def __get_project_entity(self,row):
        return Projects(id=row["id"], title=row["title"], content=row["content"], technologies=row["technologies"], link=row["link"])