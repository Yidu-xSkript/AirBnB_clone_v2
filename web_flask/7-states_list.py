#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
Jinja to render html
Routes:
    /states_list: Lists all states in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Lists all states in DBStorage."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """close the db session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")