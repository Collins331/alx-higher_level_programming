#!/usr/bin/python3
"""a class with a area() method"""


class BaseGeometry:
    """BaseGeometry class with a method"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
