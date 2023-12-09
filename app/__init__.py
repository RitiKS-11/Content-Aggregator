from flask import Flask
from celery import Celery

from app.database import init_db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
    )

    app.config['CELERYBEAT_SCHEDULE'] = {
        'background-task': {
            'task': 'scripts.task.background_task',
            'schedule': 24 * 60 * 60,  
        },
    }

    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

init_db(app)

from app import views
from scripts.task import background_task