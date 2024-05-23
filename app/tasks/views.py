from flask import Blueprint, jsonify

from app.tasks.models import Task


tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@tasks.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    response = {}

    for task in tasks:
        response[task.id] = {
            'name': task.title,
            'price': str(task.description)
        }
    return jsonify(response)
