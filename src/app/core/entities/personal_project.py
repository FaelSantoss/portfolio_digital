from core.entities.entity import Entity
from dataclasses import dataclass

@dataclass
class PersonalProject(Entity):
    title: str = None
    content: str = None
    technologies: str = None