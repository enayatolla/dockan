from config.settings.base import *
import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')

DATABASES = {
   'default': dj_database_url.config(
      default= os.getenv('DJANGO_DATABASE_URL'),
      conn_max_age=600
   )
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
   # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')