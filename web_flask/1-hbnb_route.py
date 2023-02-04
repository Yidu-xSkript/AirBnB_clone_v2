#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
Routes:
    /: Return 'Hello HBNB!'.
    /hbnb: Return 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Return 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return 'HBNB'."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")