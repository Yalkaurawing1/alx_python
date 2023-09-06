#!/usr/bin/python3

# Import the requests package
import requests

# Send a GET request to the URL
response = requests.get("https://alu-intranet.hbtn.io/status")

# Check if the request was successful
if response.status_code == 200:
    # Print the body of the response
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
else:
    # Print an error message
    print("Error: {}".format(response.status_code))
