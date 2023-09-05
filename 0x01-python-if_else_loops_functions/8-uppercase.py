#!/usr/bin/python3
def uppercase(str):
    result = ""
    for upper in str:
        if upper >= 'a' and upper <= 'z':
            string = chr(ord(upper) - 32)
            result += string
        else:
            result += upper
    print("{}".format(result))
