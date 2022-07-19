# syntax=docker/dockerfile:1
FROM python:3.7-alpine

COPY requirements.txt main.py ./
RUN pip install -r requirements.txt

CMD python /main.py