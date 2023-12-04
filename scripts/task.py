from app import celery
from .scraper import run

@celery.task
def background_task():
    run()

