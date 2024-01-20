#!/usr/bin/python3
"""import sys and requests modules"""
from sys import argv as ag
import requests

if __name__ == "__main__":
    """post data to the url using request"""
    data = {'email': ag[2]}
    r = requests.post(ag[1], data=data)
    print(r.text)
