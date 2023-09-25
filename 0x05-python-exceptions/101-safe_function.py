#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file = sys.stderr)
        result = None
        return result
