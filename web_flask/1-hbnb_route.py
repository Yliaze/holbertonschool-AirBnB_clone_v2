#!/usr/bin/python3
"""This script creates a simple Flask web application."""
from flask import Flask

"""Create an instance of the Flask application"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Return HBNB"""
    return "HBNB"


"""Start the Flask application when the script is run directly"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
