import os

from flasgger import Swagger
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from app.core.config import BaseConfig, get_config
from app.core.database import create_db


def create_app(config: BaseConfig | None = None) -> Flask:
    if config is None:
        config = get_config(os.environ.get('FLASK_CONFIG', 'DEV'))

    app = Flask(__name__)
    app.config.from_object(config)

    return app


app = create_app()
db = create_db(app)
migrate = Migrate(app, db)
marshmallow = Marshmallow(app)
swagger = Swagger(app)
