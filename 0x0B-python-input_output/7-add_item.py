#!/usr/bin/python3

"""adds all arguments to a Python list, and then save them to a file"""
import sys
"""imports sys module"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
""" imports load_from_json_file module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""imports save_to_json_file module"""

argv = sys.argv[1:]

try:
    item = load_from_json_file("add_item.json")
except FileNotFoundError:
    item = []

item.extend(argv)
save_to_json_file(item, "add_item.json")
