#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = -(number)
        y = x % 10
        print("{:d}".format(y), end='')
    else:
        x = number
        y = x % 10
        print("{:d}".format(y), end='')
    return y
