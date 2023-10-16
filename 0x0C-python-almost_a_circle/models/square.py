#!/usr/bin/python3

"""square subclass"""
from models.rectangle import Rectangle

"""import the Rectangle super class"""


class Square(Rectangle):
    """
    a square subclass that inherits
    from the Rectangle class
    its arguments are:
    size, x, y and id
    """

    def __init__(self, size, x=0, y=0, id=None):
        """instatiates the class square"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """returns the string if square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the instance attribute values"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary containing value of arguments"""
        new_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return new_dict
