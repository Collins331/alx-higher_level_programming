#!/usr/bin/pyhton3
"""
This module has a function that prints a square with the character #
"""


def print_square(size):
    """
    Checks if the parameter is an integer and prints a square with the
    character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
