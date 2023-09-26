#!/usr/bin/python3
"""a square class with methods in it"""


class Square:
    """init function"""
    def __init__(self, size=0):
        """checks if data type is int else raises TypeError"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """Raises ValueError if size is less than 0"""
        if size < 0:
            raise ValueError("size must be >= 0")
        """initializes a private attribute"""
        self.__size = size
