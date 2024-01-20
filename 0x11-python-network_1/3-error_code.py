#!/usr/bin/python3
"""import sys and urllib module"""

from urllib import request, error
import sys

if __name__ == "__main__":
    """prints the error code encountered"""
    try:
        with request.urlopen(sys.argv[1]) as response:
            data = response.read().decode('utf-8')
            print(data)

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
