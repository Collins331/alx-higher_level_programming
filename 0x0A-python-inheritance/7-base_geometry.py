#!/usr/bin/python3
"""a class with a area() method"""


class BaseGeometry:
    """BaseGeometry class with a method"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
