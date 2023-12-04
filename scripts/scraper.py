from .main import get_response, insert_in_database


def bbc_news():
    soup = get_response("https://www.bbc.com/")

    hero_content = soup.find("div", class_="media media--hero media--primary media--overlay block-link")
    img = hero_content.find("img")["src"]
    news = hero_content.find("a", class_="block-link__overlay-link")
    title = news.text.strip().replace('\n','')
    url = "https://www.bbc.com/" + news["href"]

    insert_in_database(title=title, url=url, img=img, source='bbc')

    contents = soup.find_all("div", class_="media media--overlay block-link")

    for content in contents:
        img = content.find("img")["src"]
        post = content.find("a", class_="media__link")
        title = post.text.strip().replace('\n','')
        url = "https://www.bbc.com/" + post["href"]
        insert_in_database(title=title, url=url, img=img, source='bbc')

def reddit_news():
    soup = get_response("https://www.reddit.com/r/news/")
    contents = soup.find_all("a", class_="absolute inset-0")

    for content in contents:
        url = "https://www.reddit.com" + content["href"]
        title = content["aria-label"]
        insert_in_database(title=title, url=url, source='reddit_news')

def reddit_spacex():
    soup = get_response("https://www.reddit.com/t/spacex/")
    contents = soup.find_all("a", class_="absolute inset-0")

    for index,content in enumerate(contents):
        url = "https://www.reddit.com" + content["href"]
        title = content["aria-label"]
        insert_in_database(title=title, url=url, source='reddit_spacex')

        if index == 4:
            break

def manga():
    soup = get_response("https://toonily.net/manga/?m_orderby=latest")
    manga_list = soup.find_all("div", class_="col-6 col-md-3 badge-pos-2")

    for index, manga in enumerate(manga_list):

        post = manga.find("div", class_="post-title font-title")
        title = post.text.strip().replace('\n', '')
        img = manga.find("img", class_="img-responsive")["src"]
        url = post.find("a")['href']
        
        insert_in_database(title=title, url=url, img=img, source='toonily')

        if index == 4:
            break

def anime():
    soup = get_response("https://aniwatch.to/tv")
    ul = soup.find("div", id="top-viewed-day")
    animes = ul.find_all("li")

    for index, anime in enumerate(animes):
        img = anime.find("img", class_="film-poster-img lazyload")["data-src"]
        post = anime.find("a", class_="dynamic-name")
        title = post.text
        url = "https://aniwatch.to" + post['href']

        insert_in_database(title=title, url=url, img=img, source='aniwatch')

        if index == 4:
            break


def run():
    bbc_news()
    reddit_news()
    reddit_spacex()
    manga()
    anime()