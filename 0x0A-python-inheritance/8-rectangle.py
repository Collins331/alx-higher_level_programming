#!/usr/bin/python3
"""a class with a area() method"""


class BaseGeometry:
    """BaseGeometry class with a method"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """a Rectangle class which inherits BaseGeometry"""
    def __init__(self, width, height):
        """instatiates the class"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
