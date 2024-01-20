#!/usr/bin/python3
"""import sys and requests modules"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # get the username and password from the command line
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API URL
    url = 'https://api.github.com/user'

    # authentication
    auth = HTTPBasicAuth(username, password)

    # send a GET request to the GitHub API
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
