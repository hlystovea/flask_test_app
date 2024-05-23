import os

from flask import Flask
from werkzeug.utils import import_string


config = import_string(
    os.environ.get('FLASK_CONFIG', 'src.core.config.ProdConfig')
)()

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'
