from config.settings.base import *
import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = True
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')

DATABASES = {
   'default': dj_database_url.config(
      default= os.getenv('DJNAGO_DATABASE_URL'),
   )
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


