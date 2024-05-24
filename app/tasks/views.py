from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.main import db
from app.tasks.models import Task
from app.tasks.scheme import task_schema, tasks_schema, task_update_schema


tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@tasks.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    return tasks_schema.dump(tasks)


@tasks.route('/tasks/<id>')
def retrieve_task(id: int):
    task = Task.query.get_or_404(id)
    return task_schema.dump(task)


@tasks.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    try:
        task = task_schema.load(data)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    db.session.add(task)
    db.session.commit()

    return task_schema.dump(task), 201


@tasks.route('/tasks/<id>', methods=['PUT', 'PATCH'])
def update_task(id: int):
    task = Task.query.get_or_404(id)

    try:
        task_update_schema.load(
            request.get_json(), session=db.session, instance=task, partial=True
        )
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    db.session.commit()

    return task_schema.dump(task)


@tasks.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id: int):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task successfully deleted'}), 204
