FROM python:latest

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

CMD ["gunicorn", "YoutubeBot.wsgi", ":8000"]