#!/usr/bin/python3
"""Inherits a list and prints it sorted"""


class MyList(list):
    """prints a sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
