#!/usr/bin/python3
"""writes to a text file"""


def write_file(filename="", text=""):
    """writes text to filename"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
