#!/usr/bin/python3

"""class defination"""


class Student:
    """a  student class"""

    def __init__(self, first_name, last_name, age):
        """
        an instance of class
        with three public attributes:
        first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves  a dictionary representation of a Student
        class
        """
        return self.__dict__
