#!/usr/bin/python3


class Rectangle:
    """has private attributes width and height"""
    def __init__(self, width=0, height=0):
        """instanciates the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getts the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
