#!/usr/bin/python3

# Import requests and sys modules
import requests
import sys

# Get the letter from the command line argument
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Set the q parameter to the letter
params = {"q": letter}

# Send a POST request to the server
response = requests.post("http://0.0.0.0:5000/search_user", params=params)

# Try to parse the response as JSON
try:
    data = response.json()
    # Check if the JSON is empty
    if data:
        # Display the id and name
        print("[{}] {}".format(data.get("id"), data.get("name")))
    else:
        # Display no result
        print("No result")
except ValueError:
    # Display not a valid JSON
    print("Not a valid JSON")
