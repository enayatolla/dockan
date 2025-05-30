from config.settings.base import *
import dj_database_url
import os
# env reader
from dotenv import load_dotenv
load_dotenv()


DEBUG = True
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-1234567890abcdefghijklmnopqrstuvwxyz')
ALLOWED_HOSTS = ['*']


DATABASES = {
   'default': dj_database_url.config(
      default= os.getenv('DJNAGO_DATABASE_URL'),
   )
}
