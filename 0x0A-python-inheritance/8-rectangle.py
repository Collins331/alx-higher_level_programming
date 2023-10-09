#!/usr/bin/python3
"""a class with a area() method"""


class BaseGeometry:
    """BaseGeometry class with a method"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a Rectangle class which inherits BaseGeometry"""
    def __init__(self, width, height):
        """instatiates the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
