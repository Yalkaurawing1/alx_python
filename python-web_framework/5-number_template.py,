#!/usr/bin/python3
"""Copy of the previous task to a new
script that starts a Flask web application
"""
# Import Flask and render_template
from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__)

# Define the route for /
@app.route('/', strict_slashes=False)
def hello():
    # Return the message to display
    return 'Hello HBNB!'

# Define the route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # Return the message to display
    return 'HBNB'

# Define the route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscore with space in text
    text = text.replace('_', ' ')
    # Return the message to display
    return 'C {}'.format(text)

# Define the route for /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    # Replace underscore with space in text
    text = text.replace('_', ' ')
    # Return the message to display
    return 'Python {}'.format(text)

# Define the route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # Return the message to display
    return '{} is a number'.format(n)

# Define the route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render the HTML template with n as a parameter
    return render_template('number.html', n=n)

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
