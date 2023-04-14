#!/usr/bin/python3
"""Create JSON string Module"""
import json


def from_json_string(my_str):
    """pasrse a Json string to a json object
       Args:
           my_str: json strings to parse
    """
    return (json.loads(my_str))
