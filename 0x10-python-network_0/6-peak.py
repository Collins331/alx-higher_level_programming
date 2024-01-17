#!/usr/bin/python3
"""
returns the peak number in a list
of integers
"""
def find_peak(list_of_integers):
    """
    finds the peak number in a list of
    integers
    """
    try:
        peak = max(list_of_integers)
    except ValueError:
        peak = None

    return peak
