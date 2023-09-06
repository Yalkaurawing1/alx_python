#!/usr/bin/python3

# Import requests and sys modules
import requests
import sys

url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]
parameters = (username, password)

response = requests.get(url, auth=parameters)
try:
    print(response.json()['id'])
except:
    print('None')