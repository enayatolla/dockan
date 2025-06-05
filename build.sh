#!/usr/bin/env bash
set -o errexit

poetry run python manage.py makemigrations
poetry run python manage.py migrate

poetry run python manage.py tailwind install
poetry run python manage.py tailwind build
poetry run python manage.py collectstatic --no-input --clear


poetry run python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker