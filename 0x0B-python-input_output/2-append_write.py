#!/usr/bin/python3
"""appends text to a file"""


def append_write(filename="", text=""):
    """appends text to existing contents of a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))
