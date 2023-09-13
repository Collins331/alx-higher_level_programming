#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set(my_list)
    result = 0
    for i in x:
        result += i
    return result