#!/usr/bin/python3

# Import requests and sys modules
import requests
import sys

# Get the username and password from the command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Set the authentication header with basic authentication
auth = requests.auth.HTTPBasicAuth(username, password)

# Send a GET request to the GitHub API
response = requests.get("https://api.github.com/user", auth=auth)

# Try to parse the response as JSON
try:
    data = response.json()
    # Check if the JSON has an id field
    if "id" in data:
        # Display the id
        print(data["id"])
    else:
        # Display an error message
        print("No id found")
except ValueError:
    # Display an error message
    print("Not a valid JSON")
