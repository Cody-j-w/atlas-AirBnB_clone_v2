#!/usr/bin/python3
"""
Routing module - contains data display routes
"""
import sys
from flask import Flask
from flask import render_template
from flask import g
import logging
from models import storage, env
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_route(id=0):
    res = 0
    title = "HBNB"
    if id == 0:
        res = storage.all("State").values()
    else:
        for state in storage.all("State"):
            if state.split(".")[1] == id:
                res = storage.all("State")[state]
    if id != 0 and res == 0:
        title = "Not found"
        id = 'Not found'

    return render_template("9-states.html", res=res, id=id, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
