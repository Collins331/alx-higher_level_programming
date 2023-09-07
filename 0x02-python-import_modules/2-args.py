#!/usr/bin/python3
import sys

if __name__ == "__main__":
    x = sys.argv
    y = len(x) - 1

    if y == 1:
        print("{} {}".format(y, "argument:"))
        for i in range(1, len(x)):
            print("{}: {}".format(i, x[i]))

    elif y > 1:
        print("{} {}".format(y, "arguments:"))
        for i in range(1, len(x)):
            print("{}: {}".format(i, x[i]))

    else:
        print("{} {}".format(y, "arguments."))
