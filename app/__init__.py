from flask import jsonify

from app.main import app
from app.tasks.views import tasks


app.register_blueprint(tasks)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': str(error)})
