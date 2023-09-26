#!/usr/bin/python3
"""a square class with methods in it"""


class Square:
    """init function"""
    def __init__(self, size=0):
        """initializes a private attribute"""
        self.__size = size

    """Retrieves the value from the hidden attribute"""
    @property
    def size(self):
        return self.__size

    """"sets the value retrieved to the size attribute"""
    @size.setter
    def size(self, value):
        """checks if data type is int else raises TypeError"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """Raises ValueError if size is less than 0"""
        if value < 0:
            raise ValueError("size must be >= 0")
        """initializes a public attribute"""
        self.__size = value
    """a public  method that determines the area of a square"""

    def area(self):
        """returns the area of square"""
        return self.__size ** 2
    """Compares if the Square instances are Equal"""
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
