#!/usr/bin/python3

"""subclass defination"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle subclass that inherits from
    Base super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of subclass"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """displays the instance of rectangle"""
        for i in range(self.__height):
            print('#' * self.__width)
