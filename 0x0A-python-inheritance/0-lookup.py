#!/usr/bin/python3
"""looks for available attributes and methods available in class"""


def lookup(obj):
    """return a list of attributes and methods of a class"""

    return dir(obj)
