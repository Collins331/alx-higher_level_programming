#!/usr/bin/python3

"""import request & parse from urllib and sys"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    """
    script that takes in a URL and an email,
    sends a POST request to the passed URL
    """
    encoded_email = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with request.urlopen(sys.argv[1], encoded_email) as response:
        print(response.read().decode('utf-8'))
