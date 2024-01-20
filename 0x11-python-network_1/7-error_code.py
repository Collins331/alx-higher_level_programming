#!/usr/bin/python3
"""import sys and request modules"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    script that takes in a URL, sends request to the URL and displays the body
    """
    try:
        r = requests.get(argv[1])
        if r.text is not None:
            print(r.text)
        else:
            r.raise_for_status()
    except HTTPError as e:
        print("Error code: {}".format(e.status_code))
