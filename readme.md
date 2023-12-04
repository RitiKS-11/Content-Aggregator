# Content Aggregrator

## Things to be done
------------------
1. Scrape the websites - Four web scraped
2. Configure database with postgresql, flask-sqlalchemy and alembic - configured with sqlite and flask-sqlachemy
3. Create endpoints to view the content
4. Use cron job, celery to schedule the scraping job 
5. Design the frontend
6. Learn and use docker in this project
7. Create a make commands to easily configure the project
8. Update the documentation (readme.md) 
9. Deploy the project somewhere

## Project Goals
----------------
This is built to learn about web scraping and flask.

## Technology
------------------
* Python
* Flask
* PostgreSQL
* Requests
* BeautifulSoup4
* Flask-SQLAlchemy


## Configuration
#### Install and run locally from a virtual environment
---------------
Install the required libraries
```
pip install -r requirements.txt
```

Migrate the database
```
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```

Run the project
```
python3 -m flask --app run.py run
```

## Running Locally with Docker
-------------------------
Build the images
```
docker-compose build
```

Spin up the containers
```
docker-compose up
```


## Website to Scrape
-------------------

* BBC -> Done
* Reddit -> Done
* Mangatop - Trending Today or ManagaPlus - Top Four Hottest - Done (only toonily) managplus needs javascript
* AniWatch - Most Popular Anime Today -> Done 


## Migrate Database

* flask db init
* flask db migrate
* flask db upgrade