from config.settings.base import BASE_DIR, TIME_ZONE


CELERY_BROKER_URL ='redis://redis_db:6379/0' if str(BASE_DIR) == "/app" else 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_DEFAULT_QUEUE = 'default'