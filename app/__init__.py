from app.main import app
from app.tasks.views import tasks


app.register_blueprint(tasks)
