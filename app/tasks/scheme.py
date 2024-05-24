from marshmallow_sqlalchemy import auto_field

from app.main import marshmallow
from app.tasks.models import Task


class TaskSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Task
        load_instance = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()


class TaskUpdateSchema(TaskSchema):
    title = auto_field()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
task_update_schema = TaskUpdateSchema()
