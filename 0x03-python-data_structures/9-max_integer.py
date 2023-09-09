#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        i = 0
        y = len(my_list) - 1
        while i < y:
            if my_list[i] > my_list[i + 1]:
                nexti = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = nexti
            i += 1
        return my_list[y]
