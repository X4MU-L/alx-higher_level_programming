#!/usr/bin/python3
"""Load Json Object String from file Module"""
import json


def load_from_json_file(filename):
    """load a json object string from a file
       Args:
           filename: the file with the json object string
    """
    with open(filename, encoding="UTF-8") as f:
        return (json.load(f))
