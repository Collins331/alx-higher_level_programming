#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        newlist = []
        x = len(a_dictionary) - 1
        for i in a_dictionary:
            newlist.append(a_dictionary[i])
        newlist.sort()
        for j in a_dictionary:
            if newlist[x] == a_dictionary[j]:
                return j
