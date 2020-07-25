FROM tiangolo/uvicorn-gunicorn:python3.8 as base
MAINTAINER Mangobanaani

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get -y update && apt-get -y upgrade

FROM base as packages

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /

RUN python -m pip install --upgrade pip \
    && pip install -r /requirements.txt

FROM packages as codedeploy

COPY . /app

RUN addgroup --gid 1001 --system appgroup \
    && adduser --system --uid 1001 --disabled-login --disabled-password --gecos '' appuser \
    && chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

CMD [ "gunicorn", "-w 1", "-k uvicorn.workers.UvicornWorker", "-b0.0.0.0:8000", "--log-file=-", "main:app" ]
