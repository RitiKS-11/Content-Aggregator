import requests
from bs4 import BeautifulSoup
from sqlalchemy import exc

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
    
    except exc.IntegrityError:
        pass
    
def process_content(soup, element, class_name, base_url, source, limit=4):

    use_aria_label = ['reddit news', 'reddit spacex', 'verge']
    needs_base_url = ['bbc', 'reddit news', 'reddit spacex', 'verge', 'game informer']

    contents = soup.find_all(element, class_=class_name)

    for index, content in enumerate(contents):
        if element != 'a':
            content = content.find("a")

        title = content['aira-label'] if source in use_aria_label else content.text.strip().replace("\n","")
        url = base_url + content["href"] if source in needs_base_url else content["href"]

        # insert_in_database(title=title, url=url, source=source)
        print(title, source, url)
        print('\n')

        if limit == index:
            break
        
    
