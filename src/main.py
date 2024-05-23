import os

from flask import Flask
from werkzeug.utils import import_string


config = import_string(
    f'src.core.config.{os.environ.get("FLASK_CONFIG", "ProdConfig")}'
)()

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def get_tasks():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run()
