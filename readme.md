# Content Aggregrator

## Setup Project
---------------------
Create virtual environment
```
python -m venv .venv
```

Activate virtual environment
```
source .venv/bin/activate
```

Install the required libraries
```
pip install -r requirements.txt
```

Intialize and Migrate Database
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
python -m flask --app run.py run
```

## Run Background Task

```
celery - A app.celery worker --loglevel=info
```

```
celery -A app.celery beat --loglevel=info
``` -
