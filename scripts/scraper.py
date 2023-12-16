from .main import get_response, insert_in_database, process_content


def bbc_news():
    url = "https://www.bbc.com/"
    soup = get_response(url)
    
    process_content(soup=soup, element="a", class_name="media__link", base_url = url, source='BBC')

def reddit_news():
    url = "https://www.reddit.com/r/news/"
    soup = get_response(url)

    process_content(soup=soup, element="a", class_name="absolute inset-0", base_url = url, source='reddit news')

def reddit_spacex():
    url = "https://www.reddit.com/t/spacex/"
    soup = get_response(url)

    process_content(soup=soup, element="a", class_name="absolute inset-0", base_url = url, source='reddit spacex')

def verge():
    url = "https://www.theverge.com/"
    soup = get_response(url)

    process_content(soup=soup, element="a", class_name="hover:shadow-underline-inherit after:absolute after:inset-0", base_url = url, source='verge')

def techcrunch():
    url = "https://techcrunch.com/"
    soup = get_response(url)

    process_content(soup=soup, element="a", class_name="post-block__title__link", base_url = url, source='techcrunch')


def apple_insider():
    url = "https://appleinsider.com/"
    soup = get_response(url)

    process_content(soup=soup, element="h2", class_name="blueHover", base_url=url, source="apple insider")
   

def linux_today():
    url = "https://www.linuxtoday.com/"
    soup = get_response(url)

    process_content(soup=soup, element="h3", class_name="entry-title td-module-title", base_url = url, source='linux today')


def linux():
    url = "https://www.linux.com/"
    soup =  get_response(url)

    process_content(soup=soup, element="h3", class_name="entry-title td-module-title", base_url = url, source='linux')


def game_informer():
    url = "https://www.gameinformer.com/"
    soup = get_response(url)

    process_content(soup=soup, element="h3", class_name="page-title article-title", base_url = url, source='game informer')
  

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


def run_scripts():
    bbc_news()
    reddit_news()
    reddit_spacex()
    techcrunch()
    game_informer()
    linux_today()
    # apple_insider()
    # manga()
    # anime()
    verge()

