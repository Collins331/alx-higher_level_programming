#!/usr/bin/python3
""" if the object is an instance of a subclass or class"""


def is_kind_of_class(obj, a_class):
    """return True if obj is an instance of subclass or class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
