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


@app.route("/hbnb_filters", strict_slashes=False)
def filter_route():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
