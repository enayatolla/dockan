FROM python:3.11

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod a+x build.sh
RUN ./build.sh


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]