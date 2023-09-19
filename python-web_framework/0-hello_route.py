#!/usr/bin/python3

from flask import Flask
""" Import Flask
"""
# Create an instance of Flask
app = Flask(__name__)

# Define the route for /
@app.route('/', strict_slashes=False)
def hello():
    # Return the message to display
    return 'Hello HBNB!'

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

