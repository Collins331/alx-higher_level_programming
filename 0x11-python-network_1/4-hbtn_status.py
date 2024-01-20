#!/usr/bin/python3
"""import the requests module"""

import requests as r

if __name__ == "__main__":
    """fetch details from a url"""
    res = r.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(res.text), res.text))
