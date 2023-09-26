#!/usr/bin/python3
"""a square class with methods in it"""


class Square:
    """init function"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a private attribute"""
        self.__size = size
        self.__position = position

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

    """Retrieve the private attribute"""
    @property
    def position(self):
        return self.__position
    """initializes position attribute to public"""
    @position.setter
    def position(self, value):
        """modify the attribute value"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """a public  method that determines the area of a square"""

    def area(self):
        """returns the area of square"""
        return self.__size ** 2
    """prints # """
    def my_print(self):
        """print the square to stdout with xcter ###"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print()
