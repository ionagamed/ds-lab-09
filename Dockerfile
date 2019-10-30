FROM python:3.6-alpine

WORKDIR /app
RUN pip3 install pymongo flask
CMD python3 app.py

COPY ./app.py /app
COPY ./templates /app/templates

