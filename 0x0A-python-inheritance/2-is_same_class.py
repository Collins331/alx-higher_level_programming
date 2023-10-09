#!/usr/bin/python3
""" checks if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """return true if obj is of type a_class"""
    if type(obj) is a_class:
        return True
    else:
        return False
