#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
Jinja tests - use mapping to check dictionary
Routes:
    /states: List all states on an html page.
    /states/<id>: show state based on <id> and list out cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """List all states on an html page."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """show state based on <id> and list out cities."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(exception):
    """close the db session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")