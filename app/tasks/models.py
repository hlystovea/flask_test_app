from sqlalchemy import Column, Integer, String

from app.services.database import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(400))

    def __init__(self, title, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
