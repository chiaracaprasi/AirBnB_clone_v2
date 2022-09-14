#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """returns C followed by value of text"""
    return f'C' + text.replace("_", " ")


@app.route('/c/<text>', strict_slashes=False)
def show_text_cool(text='is cool'):
    """returns C followed by value of text"""
    return f'C' + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
