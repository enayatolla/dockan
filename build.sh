#!/usr/bin/env bash
set -o errexit

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker