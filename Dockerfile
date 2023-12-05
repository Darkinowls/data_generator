FROM python:3.9-alpine
LABEL authors="Denys"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
