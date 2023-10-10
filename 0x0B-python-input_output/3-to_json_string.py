#!/usr/bin/python3

"""Converts string object to JSON"""
import json
"""import json module"""


def to_json_string(my_obj):
    """
    converts string object to JSON represention
    and return the JSON
    """
    return (json.dumps(my_obj))
