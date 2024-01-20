#!/usr/bin/python3
"""import sys and urllib module"""

from urllib import request, error
import sys

try:
    with request.urlopen(sys.argv[1]) as respose:
        data = response.read()

except error.HTTPError as e:
    print("Error code: {}".format(e.code))
