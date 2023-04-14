#!/usr/bin/python3
"""Covert Class to JSON object"""


def class_to_json(obj):
    """returns a json/dict repsentation of an object
       args:
           obj: instance of a class
    """
    return obj.__dict__
