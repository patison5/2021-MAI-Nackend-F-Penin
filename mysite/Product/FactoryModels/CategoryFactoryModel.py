from dataclasses import dataclass

@dataclass
class Post:
    title: str
    description: str
    published: bool
    image: str