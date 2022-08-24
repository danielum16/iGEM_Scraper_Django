# syntax=docker/dockerfile:1
FROM python:3.8.13-alpine3.16
RUN apk add build-base
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]