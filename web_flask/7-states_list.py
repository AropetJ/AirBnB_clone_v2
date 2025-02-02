#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page: (inside the tag BODY)
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown(exception):
    """Closes the storage engine on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
