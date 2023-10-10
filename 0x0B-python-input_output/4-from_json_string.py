#!/usr/bin/python3

"""JSON to string"""
import json
"""imports json module"""


def from_json_string(my_str):
    """
    returns  an object represented
    by a JSON string
    """
    return (json.loads(my_str))
