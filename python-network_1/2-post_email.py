#!/usr/bin/python3

# Import the requests and sys packages
import requests
import sys

# Get the URL and the email from the first and second arguments
url = sys.argv[1]
email = sys.argv[2]

# Send a POST request to the URL with the email as a parameter
response = requests.post(url, data={"email": email})

# Print the body of the response
print(response.text)
