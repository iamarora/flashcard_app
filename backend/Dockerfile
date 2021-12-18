FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /backend

COPY requirements.txt /backend/
RUN pip install -r requirements.txt
