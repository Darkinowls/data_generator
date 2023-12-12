FROM python:3.9-alpine as dark
LABEL authors="Denys"

COPY . /app

WORKDIR /app

ENV TZ=America/New_York

ENV TOPIC="tv_house"

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
