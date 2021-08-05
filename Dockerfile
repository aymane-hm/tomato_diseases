FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT python3 app.py


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app