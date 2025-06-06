#! /bin/bash

poetry run python manage.py migrate

poetry run python manage.py tailwind install
poetry run python manage.py tailwind build
poetry run python manage.py collectstatic --no-input --clear

poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000
