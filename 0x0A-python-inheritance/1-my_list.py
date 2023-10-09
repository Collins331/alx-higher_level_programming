#!/usr/bin/python3
"""Inherits a list and prints it sorted"""


class MyList(list):
    """initializes the sub class"""
    def __init__(self):
        """supper class is instatiated"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
