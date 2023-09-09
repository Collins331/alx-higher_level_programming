#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = -(len(my_list))
    i = -1
    while i >= x:
        print("{:d}".format(my_list[i]))
        i -= 1
