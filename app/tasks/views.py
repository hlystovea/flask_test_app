from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.main import db
from app.tasks.models import Task
from app.tasks.schemes import task_schema, tasks_schema, task_update_schema


tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks')
def get_tasks():
    """
    Returning a list of tasks
    ---
    definitions:
        Tasks:
            type: array
            items:
                $ref: '#/definitions/Task'
        Task:
            type: object
            properties:
                id:
                    type: integer
                title:
                    type: string
                    description: The title of the task
                description:
                    type: string
                    description: The description of the task
                created_at:
                    type: string
                    description: The date when the task was created
                updated_at:
                    type: string
                    description: The date when the task was updated
    responses:
        200:
            description: A list of tasks
            schema:
                $ref: '#/definitions/Tasks'
            examples:
                ['red', 'green', 'blue']
    """
    tasks = Task.query.all()
    return tasks_schema.dump(tasks)


@tasks.route('/tasks/<id>')
def get_task(id: int):
    """
    Returning a task by id
    ---
    parameters:
        - in: path
          name: id
          type: integer
          required: true
    definitions:
        Task:
            type: object
            properties:
                id:
                    type: integer
                title:
                    type: string
                    description: The title of the task
                description:
                    type: string
                    description: The description of the task
                created_at:
                    type: string
                    description: The date when the task was created
                updated_at:
                    type: string
                    description: The date when the task was updated
    responses:
        200:
            description: A task
            schema:
                $ref: '#/definitions/Task'
            examples:
                {
                    'id': 0,
                    'title': 'title',
                    'description': 'description',
                    'created_at': '2024-01-01T00:00:00',
                    'updated_at': '2024-01-01T00:00:00'
                }
    """
    task = Task.query.get_or_404(id)
    return task_schema.dump(task)


@tasks.route('/tasks', methods=['POST'])
def create_task():
    """
    Creating and returning a new task
    ---
    parameters:
        - in: body
          name: title
          type: string
          name: description
          type: string
    definitions:
        Task:
            type: object
            properties:
                id:
                    type: integer
                title:
                    type: string
                    description: The title of the task
                description:
                    type: string
                    description: The description of the task
                created_at:
                    type: string
                    description: The date when the task was created
                updated_at:
                    type: string
                    description: The date when the task was updated
    responses:
        201:
            description: New task
            schema:
                $ref: '#/definitions/Task'
            examples:
                {
                    'id': 0,
                    'title': 'title',
                    'description': 'description',
                    'created_at': '2024-01-01T00:00:00',
                    'updated_at': '2024-01-01T00:00:00'
                }
    """
    data = request.get_json()

    try:
        task = task_schema.load(data)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    db.session.add(task)
    db.session.commit()

    return task_schema.dump(task), 201


@tasks.route('/tasks/<id>', methods=['PUT'])
def update_task(id: int):
    """
    Updating a task by id
    ---
    parameters:
        - in: path
          name: id
          type: integer
    definitions:
        Task:
            type: object
            properties:
                id:
                    type: integer
                title:
                    type: string
                    description: The title of the task
                description:
                    type: string
                    description: The description of the task
                created_at:
                    type: string
                    description: The date when the task was created
                updated_at:
                    type: string
                    description: The date when the task was updated
    responses:
        200:
            description: Modified task
            schema:
                $ref: '#/definitions/Task'
            examples:
                {
                    'id': 0,
                    'title': 'title',
                    'description': 'description',
                    'created_at': '2024-01-01T00:00:00',
                    'updated_at': '2024-01-01T00:00:00'
                }
    """
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
    """
    Deleting a task by id
    ---
    parameters:
        - in: path
          name: id
          type: integer
    responses:
        200:
            description: A message about a successful operation
            schema:
                type: object
                properties:
                    message:
                        type: string
            examples:
                {'message': 'Task successfully deleted'}
    """
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task successfully deleted'})
