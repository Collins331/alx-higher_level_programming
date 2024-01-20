#!/usr/bin/python3
import urllib.request

"""module that sends requests to urls"""

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()

print(
    "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
        type(body), body, body.decode("utf-8")
    )
)
