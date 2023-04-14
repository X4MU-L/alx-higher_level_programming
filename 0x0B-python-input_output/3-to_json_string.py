#!/usr/bin/python3
"""Create JSON string Module"""
import json


def to_json_string(my_obj):
    """pasrse a Json serializable to a string
       Args:
           my_obj: json object to parse
    """
    return (json.dumps(my_obj))
