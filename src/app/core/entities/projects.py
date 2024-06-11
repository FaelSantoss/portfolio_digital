from core.entities.entity import Entity
from dataclasses import dataclass

@dataclass
class Projects(Entity):
    title: str = None
    content: str = None
    technologies: str = None
    link: str = None
    img: str = None