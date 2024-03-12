#!/usr/bin/python3
"""
Routing module - contains data display routes
"""
import sys
from flask import Flask
from flask import render_template
from flask import g
import logging
sys.path.append(".")
from models import storage, env
from models.state import State
from models.city import City

app = Flask(__name__)

@app.teardown_appcontext(Exception)
def teardown():
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_route():
    if env == 'db':
        states = storage.all("State").values()
    else:
        pass

    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
