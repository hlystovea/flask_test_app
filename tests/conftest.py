import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.core.config import get_config
from app.core.database import create_db
from app.main import create_app
from app.tasks.schemes import task_schema
from app.tasks.views import tasks


@pytest.fixture(scope='class')
def app():
    config = get_config('TEST')
    app = create_app(config)
    app.register_blueprint(tasks)
    yield app


@pytest.fixture(scope='class')
def db(app: Flask):
    db = create_db(app)
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='class')
def client(app: Flask):
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='function')
def task_1(db: SQLAlchemy):
    data = {'title': 'title_1', 'description': 'description_1'}
    task = task_schema.load(data)
    db.session.add(task)
    db.session.commit()
    return task


@pytest.fixture(scope='function')
def task_2(db: SQLAlchemy):
    data = {'title': 'title_2'}
    task = task_schema.load(data)
    db.session.add(task)
    db.session.commit()
    return task
