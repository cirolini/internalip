FROM python:2-stretch

WORKDIR /app
COPY . /app
RUN pip install -e .

EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
