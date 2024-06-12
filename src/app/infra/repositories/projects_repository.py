
from core.commons import Error

class ProjectsRepository: 
    def get_projects_by_title(self, title, data):
        for project in data:
            if project['title'] == title:
                return project

        return None

    def get_icons_by_technologies(self, technologies):
        try:
            technologies_icons = []
            for technologie in technologies:
                    technologies_icons.append(f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{technologie}/{technologie}-original.svg")
        except Error as error:
            raise error
        
        return technologies_icons