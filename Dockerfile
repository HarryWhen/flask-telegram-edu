# syntax=docker/dockerfile:1
FROM python:3.12-slim
WORKDIR /app
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["flask", "run"]
