#!/usr/bin/python3


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (int, boolean, list, dict, string)
    for JSON serialization of an object
    """
    return obj.__dict__
