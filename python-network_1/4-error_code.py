#!/usr/bin/python3

# Import the requests and sys packages
import requests
import sys

# Get the URL from the first argument
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Check if the HTTP status code is greater than or equal to 400
if response.status_code >= 400:
    # Print an error message with the status code
    print("Error code: {}".format(response.status_code))
else:
    # Print the body of the response
    print(response.text)
