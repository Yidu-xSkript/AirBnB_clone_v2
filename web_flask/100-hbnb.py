#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
escape html on jinja using |safe
Routes:
    /hbnb: display a HTML page like 8-index.html,-
    done during the 0x01. AirBnB clone - Web static project
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays an html page from AirBnB clone."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown(exception):
    """close the db session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")