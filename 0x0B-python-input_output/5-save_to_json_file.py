#!/usr/bin/python3
"""Create JSON string Module"""
import json


def save_to_json_file(my_obj, filename):
    """pasrse a Json serializable to a string and write to a file
       Args:
           my_obj: json object to parse
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
