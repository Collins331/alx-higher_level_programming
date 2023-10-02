#!/usr/bin/python3
"""
This module has a function that takes two string parameters
and output the full name from the parameters:
firstname and lastname
"""


def say_my_name(first_name, last_name=""):
    """
    Checks if the parameters are strings and prints the full name
    else raise a TypeError with a message
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
