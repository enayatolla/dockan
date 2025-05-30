from config.settings.base import *

DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres' if str(BASE_DIR) == "/app" else 'localhost',
        'PORT': '5432',
    }
}
