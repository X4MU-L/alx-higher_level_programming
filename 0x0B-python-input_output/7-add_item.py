#!/usr/bin/python3
"""Load and Dump json string and json object from a file"""
import sys


if __name__ == "__main__":

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        newarr = load_from_json_file("add_item.json")
    except FileNotFoundError:
        newarr = []
    newarr.extend(sys.argv[1:])
    save_to_json_file(newarr, "add_item.json")
