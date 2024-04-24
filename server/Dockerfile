FROM python:latest


MAINTAINER MrParsiphal


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"


RUN pip install django
RUN pip install gunicorn
RUN pip install mysqlclient
RUN pip install mutagen
RUN pip install Pillow


EXPOSE 5532