from .main import get_response, insert_in_database, process_content


def bbc_news():
    url = "https://www.bbc.com/"
    soup = get_response(url)
    element = "a"
    class_name = "media__link"

    process_content(soup=soup, element=element, class_name=class_name, base_url = url, source='BBC')

    # hero_content = soup.find("div", class_="media media--hero media--primary media--overlay block-link")
    # img = hero_content.find("img")["src"]
    # news = hero_content.find("a", class_="block-link__overlay-link")
    # title = news.text.strip().replace('\n','')
    # url = "https://www.bbc.com/" + news["href"]

    # insert_in_database(title=title, url=url, img=img, source='bbc')

    # contents = soup.find_all("div", class_="media media--overlay block-link")

    # process_content(soup=soup, element="div", class_name="media media--overlay block-link", source="BBC")

    # for content in contents:
    #     img = content.find("img")["src"]
    #     post = content.find("a", class_="media__link")
    #     title = post.text.strip().replace('\n','')
    #     url = "https://www.bbc.com/" + post["href"]
    #     insert_in_database(title=title, url=url, img=img, source='bbc')

def reddit_news():
    url = "https://www.reddit.com/r/news/"
    soup = get_response(url)
    process_content(soup=soup, element="a", class_name="absolute inset-0", base_url = url, source='reddit news')
    # contents = soup.find_all("a", class_="absolute inset-0")

    # for content in contents:
    #     url = "https://www.reddit.com" + content["href"]
    #     title = content["aria-label"]
    #     insert_in_database(title=title, url=url, source='reddit_news')

def reddit_spacex():
    url = "https://www.reddit.com/t/spacex/"
    soup = get_response(url)
    process_content(soup=soup, element="a", class_name="absolute inset-0", base_url = url, source='reddit spacex')
    # contents = soup.find_all("a", class_="absolute inset-0")

    # for index,content in enumerate(contents):
    #     url = "https://www.reddit.com" + content["href"]
    #     title = content["aria-label"]
    #     insert_in_database(title=title, url=url, source='reddit_spacex')

    #     if index == 4:
    #         break

def verge():
    url = "https://www.theverge.com/"
    soup = get_response(url)
    process_content(soup=soup, element="a", class_name="hover:shadow-underline-inherit after:absolute after:inset-0", base_url = url, source='verge')
    # contents = soup.find_all("a", class_="hover:shadow-underline-inherit after:absolute after:inset-0")

    # for content in contents:
    #     url = "https://www.theverge.com/" + content["href"]
    #     title = content["aria-label"]

    #     insert_in_database(title=title, url=url, source='verge')


def techcrunch():
    url = "https://techcrunch.com/"
    soup = get_response(url)
    process_content(soup=soup, element="a", class_name="post-block__title__link", base_url = url, source='techcrunch')
    # contents = soup.find_all("a", class_="post-block__title__link")

    # for content in contents:
    #     url = content['href']
    #     title = content.text

    #     insert_in_database(title=title, url=url, source='techcrunch')


def apple_insider():
    url = "https://appleinsider.com/"
    soup = get_response(url)

    process_content(soup=soup, element="h2", class_name="blueHover", base_url=url, source="apple insider")
    # contents = soup.find_all("h2", class_="blueHover")
    
    # for content in contents:
    #     content = content.find("a")
    #     url = content["href"]
    #     title = content.text

    #     insert_in_database(title=title, url=url, source='apple_insider')        

def linux_today():
    url = "https://www.linuxtoday.com/"
    soup = get_response(url)
    process_content(soup=soup, element="h3", class_name="entry-title td-module-title", base_url = url, source='linux today')
    # contents = soup.find_all("h3", class_="entry-title td-module-title")
    
    # for content in contents:
    #     content = content.find("a")
    #     url = content["href"]
    #     title = content.text
        
    #     insert_in_database(title=title, url=url, source='linux_today')  

def linux():
    url = "https://www.linux.com/"
    soup =  get_response(url)
    process_content(soup=soup, element="h3", class_name="entry-title td-module-title", base_url = url, source='linux')
    # contents = soup.find_all("h3", class_="entry-title td-module-title")

    # for index, content in enumerate(contents):
    #     content = content.find("a")
    #     url = content["href"]
    #     title = content.text

    #     insert_in_database(title=title, url=url, source='linux') 

    #     if index == 4:
    #         break
    

def game_informer():
    url = "https://www.gameinformer.com/"
    soup = get_response(url)
    process_content(soup=soup, element="h3", class_name="page-title article-title", base_url = url, source='game informer')
    # contents = soup.find_all("h3", "page-title article-title")

    # for content in contents:
    #     content = content.find("a")
    #     url = "https://www.gameinformer.com/" + content["href"]
    #     title = content.text
        
    #     insert_in_database(title=title, url=url, source='game_informer')  

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
    # reddit_news()
    reddit_spacex()
    verge()
    techcrunch()
    game_informer()
    linux_today()
    apple_insider()
    # manga()
    # anime()
