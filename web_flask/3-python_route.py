#!/usr/bin/python3
"""
Module containing flask script with api route that displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    new_str = ""
    for i in text:
        if i == "_":
            new_str = new_str + " "
        else:
            new_str = new_str + i
    return 'C {}'.format(new_str)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    new_str = ""
    for i in text:
        if i == "_":
            new_str = new_str + " "
        else:
            new_str = new_str + i
    return "Python {}".format(new_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
