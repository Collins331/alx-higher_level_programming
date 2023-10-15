#!/usr/bin/python3

"""base class defination"""

import json
"""imports json module"""


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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json string to a file"""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_string)
