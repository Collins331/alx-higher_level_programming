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
    if len(list_of_integers) == 0:
        return None
    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)

def find_peak_helper(list_of_integers, low, high):
    """
    helper function for find_peak
    """
    if low == high:
        return list_of_integers[low]
    mid = (low + high) // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak_helper(list_of_integers, low, mid)
    return find_peak_helper(list_of_integers, mid + 1, high)

