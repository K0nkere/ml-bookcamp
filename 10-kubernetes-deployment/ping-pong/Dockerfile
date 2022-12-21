FROM python:3.9.12-slim

WORKDIR /app

RUN pip install -U pip
RUN pip install pipenv

COPY app.py .
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"]