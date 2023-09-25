#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        total = 0
        for i in my_list[:x]:
            print("{:d}".format(i), end="")
            total += 1
        return total
    except IndexError:
        pass
    finally:
        print()
