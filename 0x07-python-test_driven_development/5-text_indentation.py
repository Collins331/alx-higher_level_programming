#!/usr/bin/python3
"""
This module contains a function that prints a string of the given text
"""


def text_indentation(text):
    """
    This function prints a string of the given text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end="")
