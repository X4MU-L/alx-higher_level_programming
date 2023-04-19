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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a the string list representation of of objects in
        list_objs saving the files in <Class name>.json - example:
        Rectangle.json
        Args:
            list_objs: a list of Base objects
        """
        if list_objs is None:
            with open("{}.json".format(cls.__name__), "w",
                      encoding="UTF-8") as f:
                f.write("[]")
        else:
            with open("{}.json".format(cls.__name__), "w",
                      encoding="UTF-8") as f:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns a list representation of a json string
        args:
            json_string: a json string from which to return a json
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a subclass using a keyword argument
        args:
            dictionary: a keyword argument in key/value pairs
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
