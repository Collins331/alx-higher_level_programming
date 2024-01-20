#!/usr/bin/python3

"""module that sends requests to urls"""
import sys
import urllib.request

if __name__ == "__main__":
    """import the sys module and urllib module"""

    with urllib.request.urlopen(sys.argv[1]) as response:
        """open the url and save the response"""
        print(response.headers.get('X-Request-Id'))
