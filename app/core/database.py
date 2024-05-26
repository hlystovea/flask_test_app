from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_db(app: Flask):
    db.init_app(app)
    return db
