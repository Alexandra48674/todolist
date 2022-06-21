FROM ubuntu
RUN apt update -y && apt install -y python3-dev python3-pip

WORKDIR /todo
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN python3 ./manage.py migrate

ENV PORT=8000
CMD gunicorn todo.wsgi:application --bind 0.0.0.0:$PORT
