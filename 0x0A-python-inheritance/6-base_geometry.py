#!/usr/bin/python3
"""a class with a area() method"""


class BaseGeometry:
    """BaseGeometry class with a method"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")
