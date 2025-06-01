FROM python:3.12


WORKDIR /app

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod a+x build.sh

# Expose port 8000 for the application
EXPOSE 8000

CMD ["./build.sh"]