#!/usr/bin/python3
""" if the object is an instance of a subclass or class"""


def inherits_from(obj, a_class):
    """return True if obj is an instance of subclass or class"""
    return isinstance(obj, a_class) and not obj.__class__ == a_class
