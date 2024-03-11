#!/usr/bin/python3
"""
Routing module - contains data display routes
"""
import sys
sys.path.append(".")

from flask import Flask
from flask import render_template
from flask import g
import logging
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_route():
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
