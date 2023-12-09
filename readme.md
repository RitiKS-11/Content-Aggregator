# Content Aggregrator
This project, content aggregrator collects content form diffrenet sources and puts in a single place.


## Run with Docker

```
docker-compose up
```

## Setup Project
---------------------
Clone the project
```
git clone https://github.com/RitiKS-11/Content-Aggregator.git
```

Create virtual environment
```
python -m venv .venv
```

Activate virtual environment
```
source .venv/bin/activate
```

Install the dependencies
```
pip install -r requirements.txt
```

## Intialize and Migrate Database
```
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```

## Run Background Task

```
celery - A app.celery worker --loglevel=info
```

```
celery -A app.celery beat --loglevel=info
``` 

## Run the project
```
python -m flask --app run.py run
```