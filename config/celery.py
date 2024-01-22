from celery import Celery
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery("config")
app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()
app.conf.beat_schedule = {
   'task_beat_schedule':{
      'task': 'apps.shop.tasks.taskCeleryTwo',
      'schedule': 2 
      # 'options': {
      #    'expires': 10
      # }
   }
}




