FROM python:3.9.12-slim

WORKDIR /app
COPY ["gateway.py", "proto.py", "Pipfile", "Pipfile.lock", "./"]

RUN pip install -U pip
RUN pip install pipenv

RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "gateway:app" ]