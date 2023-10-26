#!/usr/bin/python3
"""
A script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)



@app.teardown_appcontext
def tearDown(exception):
    """Closes the storage engine on teardown"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Passes states and cities sorted by name and amenities"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
