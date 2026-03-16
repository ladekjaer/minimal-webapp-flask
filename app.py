import os
from flask import Flask, send_from_directory, url_for
import psycopg

# Establish a persistent connection
conn = psycopg.connect(os.environ['DATABASE_URL'])
conn.autocommit = True

app = Flask(__name__)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/timestamp')
def get_timestamp():
    with conn.cursor() as cur:
        cur.execute("SELECT NOW();")
        record = cur.fetchone()
        return record[0].isoformat()


if __name__ == '__main__':
    app.run()
