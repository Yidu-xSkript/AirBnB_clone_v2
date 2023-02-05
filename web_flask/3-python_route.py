#!/usr/bin/python3
"""
The app listens on 0.0.0.0, port 5000.
Routes:
    /: Return 'Hello HBNB!'.
    /hbnb: Return 'HBNB'.
    /c/<text>: gets <text> from route and concat 'C' with <text>.
    /python/(<text>): gets <text> from route and-
    concat 'Python' with <text>.
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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    gets <text> from route and concat 'C' with <text>.
    Replaces underscores in <text> with slashes.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    default value <text> => "is cool"
    gets <text> from route and concat 'Python' with <text>.
    Replaces underscores in <text> with slashes.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
