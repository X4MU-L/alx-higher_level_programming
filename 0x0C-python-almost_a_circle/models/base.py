#!/usr/bin/python3
"""Create a Base Module"""
import json


class Base:
    """Define a Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inialize a Base Object
           set id to id if id is not None
           args:
               id: (any) the id of the Base object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a string representaion of a list of dicts
        args:
            list_dictionaries: a list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
