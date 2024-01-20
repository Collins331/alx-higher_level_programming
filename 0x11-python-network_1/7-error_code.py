#!/usr/bin/python3
"""import sys and request modules"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    script that takes in a URL, sends request to the URL and displays the body
    """
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
