FROM python:3.11.7-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

RUN export FLASK_APP=run.py

# RUN flask db init && flask db migrate && flask db upgrade

# CMD ["flask", "--app", "run.py", "run", "-h", "0.0.0.0", "-p", "5000"]

CMD ["flask", "run", "-h", "0.0.0.0"]