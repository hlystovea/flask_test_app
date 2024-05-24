import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from werkzeug.utils import import_string


config_class_name = os.environ.get('FLASK_CONFIG', 'ProdConfig')
config = import_string(f'app.core.config.{config_class_name}')()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    return app


app = create_app()
migrate = Migrate(app, db)
marshmallow = Marshmallow(app)
