#!/usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (int, boolean, list, dict, string)
    for JSON serialization of an object
    args:
        obj: is an instance of a Class
        All attributes of the obj Class are serializable:
    """
    return obj.__dict__
