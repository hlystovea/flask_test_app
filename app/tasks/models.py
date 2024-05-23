from app.main import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(400))

    def __init__(self, title, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
