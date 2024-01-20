#!/usr/bin/python3
import sys
import urllib.request

if __name__ == "__main__":
    """import the sys module and urllib module"""

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()

    print(header['X-Request-Id'])
