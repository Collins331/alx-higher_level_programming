#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
a and b must be integers or floats, otherwise raise a TypeError exception
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers.
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
