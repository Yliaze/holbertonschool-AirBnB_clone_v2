#!/usr/bin/python3
"""This script creates a simple Flask web application."""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

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


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python_defaults(text):
    """display “Python ”, followed by the value of the <text> variable
    (default value is “is cool”)"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display “n is a number” only if n is an integer"""
    if type(n) is int:
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_HTMLpageint(n):
    """display a HTML page only if n is an integer"""
    if type(n) is int:
        return render_template("5-number.html", n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """function called with /states_list route that display a
    HTML page with the list of all State objects present in DBStorage"""
    list_states = storage.all("State")
    return render_template('7-states_list.html', states=list_states)


@app.teardown_appcontext
def teardown(err):
    """remove the current session"""
    storage.close()


"""Start the Flask application when the script is run directly"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
