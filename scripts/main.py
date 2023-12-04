import requests
from bs4 import BeautifulSoup

from app import app
from app.database import db
from app.models import ContentModel


def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    except Exception as e:
        raise e
    
def insert_in_database(source=None, title=None, url=None, img=None):
    try:
        with app.app_context():
            content = ContentModel(title=title, url=url, image=img, source=source)
            db.session.add(content)
            db.session.commit()
    
    except Exception as e:
        raise e