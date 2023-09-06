#!/usr/bin/python3

# Import the requests and sys packages
import requests
import sys

# Get the URL from the first argument
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Get the value of the X-Request-Id variable from the response header
x_request_id = response.headers.get("X-Request-Id")

# Print the value of the X-Request-Id variable
print(x_request_id)
