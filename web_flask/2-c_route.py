#!/usr/bin/python3
"""This script creates a simple Flask web application."""
from flask import Flask
from markupsafe import escape

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


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """display “C ” followed by the value of the <text> variable
    (replace underscore symbols with a space)"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


"""Start the Flask application when the script is run directly"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
