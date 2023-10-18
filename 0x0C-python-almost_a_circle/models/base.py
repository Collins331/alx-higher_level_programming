#!/usr/bin/python3
"""base class defination"""

import csv
import turtle
import json
"""imports json module"""
""" imports the csv module"""


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
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json string to a file"""
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """prints a list from a json string representation"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                lists = cls.from_json_string(file.read())
            return [cls.create(**dic) for dic in lists]
        except FileNotFoundError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves the file with a csv extension
        (serializes the list object
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for ob in list_objs:
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
            elif cls.__name__ == "Square":
                for ob in list_objs:
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        loads an object list from a csv file
        deserializes the file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                objects = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]))
                        obj.id = int(row[0])
                        obj.x = int(row[3])
                        obj.y = int(row[4])
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]))
                        obj.id = int(row[0])
                        obj.x = int(row[2])
                        obj.y = int(row[3])
                    objects.append(obj)
                return objects
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.
        Args:
        list_rectangles (list): A list of Rectangle objects to draw.
        list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
