#!/usr/bin/env bash
set -o errexit

# pip install -r requirements.txt # docker build will handle this

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker