FROM python:3.10.5-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

WORKDIR /app/


COPY . /app/
RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
