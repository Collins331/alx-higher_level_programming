#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for i in my_list:
        if i == search:
            i = replace
            newlist.append(i)
        else:
            newlist.append(i)
    return newlist
