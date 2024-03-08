#!/usr/bin/python3
"""
Module containing flask script with api route that displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)

@app.route('/hbnb')
def hello_world():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
