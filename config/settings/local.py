from config.settings.base import *
import dj_database_url
import os
# env reader
from dotenv import load_dotenv
load_dotenv()


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-1234567890abcdefghijklmnopqrstuvwxyz')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

if DEBUG:
   INSTALLED_APPS += ['django_browser_reload']
   MIDDLEWARE.insert(0, 'django_browser_reload.middleware.BrowserReloadMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
