#!/usr/bin/python3
"""Inherits a list and prints it sorted"""


class MyList(list):
    """initializes the sub class"""
    def print_sorted(self):
        """prints a list"""
        print(sorted(self))
