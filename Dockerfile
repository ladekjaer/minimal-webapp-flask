FROM python:latest

WORKDIR /app

COPY app.py .
COPY static static

RUN pip install flask
RUN pip install psycopg

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
