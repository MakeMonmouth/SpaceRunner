# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1

ENV SPACERUNNER_ADMIN_USER=""
ENV SPACERUNNER_ADMIN_PASS=""
ENV SPACERUNNER_ADMIN_EMAIL=""

RUN apt update && apt upgrade -y
RUN apt install -y gcc libmariadbclient-dev libsqlite3-dev libpq-dev
WORKDIR /opt/app
COPY . /opt/app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN rm -rf /opt/app/data/*.sqlite3

EXPOSE 8000

ENTRYPOINT ["./scripts/runserver.sh"]
