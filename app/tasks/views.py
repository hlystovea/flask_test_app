from flask import Blueprint, jsonify

from app.main import db
from app.tasks.models import Task


tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@tasks.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    response = {}

    response = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description
        }
        for task in tasks
    ]
    return jsonify(response)


@tasks.route('/tasks/<id>')
def retrieve_task(id: int):
    task = Task.query.get_or_404(id)
    return jsonify(title=task.title, description=task.description)


@tasks.route('/tasks', methods=['POST'])
def create_task():
    task = Task(title='123', description='')
    db.session.add(task)
    db.session.commit()
    return 'Task created'


@tasks.route('/tasks/<id>', methods=['PUT'])
def update_task(id: int):
    task = Task.query.get_or_404(id)
    task.title = '123'
    task.description = 'gh24353'
    db.session.commit()
    return 'Task updated'


@tasks.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id: int):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return 'Task deleted'
