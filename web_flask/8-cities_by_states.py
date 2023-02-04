#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: list all states and cities that are
    in relationship with the states.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """list all states and cities that are
    in relationship with the states.
    Display the result inside an html page.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """Close the db session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")