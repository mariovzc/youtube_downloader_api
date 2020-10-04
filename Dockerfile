FROM python:3.8.4-alpine3.12

RUN apk update \
    && apk add --update build-base \
    && apk add --no-cache libffi-dev \
    && apk add --no-cache tzdata

WORKDIR /app-run

COPY requirements.txt /app-run/requirements.txt
RUN pip install -r /app-run/requirements.txt

WORKDIR /app-run
COPY . /app-run

EXPOSE 8000

CMD uvicorn server:app --reload --port=8000 --host=0.0.0.0