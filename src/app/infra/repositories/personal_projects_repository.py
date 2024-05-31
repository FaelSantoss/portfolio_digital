from core.entities.personal_project import PersonalProject
from infra.database import mysql

class PersonalProjectsRepository:
    def get_personal_projects(self) -> list[PersonalProject]:
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', flush=True)
        select_query = "SELECT * FROM personal_project"
        rows = mysql.query(sql=select_query, is_single=False)

        personal_projects = []

        for row in rows:
            personal_projects.append(PersonalProject(id=row["id"], title=row["title"], content=row["content"], technologies=row["technologies"]))

        return personal_projects