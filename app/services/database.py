import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from werkzeug.utils import import_string


config_class_name = os.environ.get('FLASK_CONFIG', 'ProdConfig')
config = import_string(f'app.core.config.{config_class_name}')()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import app.tasks.models
    Base.metadata.create_all(bind=engine)
