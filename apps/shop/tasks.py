from config.celery import app
from datetime import datetime, timedelta
import time
from celery import shared_task



   
   
@app.task
def taskCelery ():
   timeStart = datetime.now()
   time.sleep(10)
   processTime = datetime.now() - timeStart
   print(f"process time : { processTime}")
   print("________________________________")
   
   
@app.task
def taskCeleryTwo ():
   timeStart = datetime.now()
   time.sleep(1)
   processTime = datetime.now() - timeStart
   
   print(f"process time shared_task : {processTime}")
   
   