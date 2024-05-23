import os

from flask import Flask
from werkzeug.utils import import_string

from app.services.database import init_db
from app.tasks.views import tasks


def get_app() -> Flask:
    config_class_name = os.environ.get('FLASK_CONFIG', 'ProdConfig')
    config = import_string(f'app.core.config.{config_class_name}')()

    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(tasks)

    init_db()
    return app


app = get_app()
