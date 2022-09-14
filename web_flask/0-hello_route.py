#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/hello', strict_slashes=False)
def hello():
    return '<h1>Hello HBNB</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)