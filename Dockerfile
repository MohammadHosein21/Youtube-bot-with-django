FROM python:3.10-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITTENBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential libpq-dev
RUN rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]