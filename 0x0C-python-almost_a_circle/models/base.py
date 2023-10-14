#!/usr/bin/python3

"""base class defination"""


class Base:
    """
    the base class that will be used as 
    a super class to manage id of future 
    classes,
    it has a private attribute:
        __n_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class initialization"""
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
