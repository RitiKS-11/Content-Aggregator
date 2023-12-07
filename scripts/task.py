from app import celery
# from .scraper import run_scripts

@celery.task
def background_task():
    run_scripts()

