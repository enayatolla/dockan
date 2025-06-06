#! /bin/bash

poetry run python manage.py makemigrations
poetry run python manage.py migrate

poetry run python manage.py tailwind build
poetry run python manage.py collectstatic --no-input --clear


# poetry run python manage.py runserver 0.0.0.0:8000
# poetry run python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000
