#!/usr/bin/python3
"""Create a Base Module"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """return a list of cls intances using a json object loaded
        from a file <Class name>.json - example: Rectangle.json
        """
        filename = "{}.json".format(cls.__name__)
        list_objs = []
        try:
            with open(filename, encoding="UTF-8") as f:
                list_objs = f.read()
        except FileNotFoundError:
            return list_objs
        list_objs = cls.from_json_string(list_objs)
        return ([cls.create(**obj) for obj in list_objs])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a list of object dicts to a csv file
        Args:
            list_objs: list of class object dicts
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """load a list of class object dicts from a file and create
        instances of class with the list and a list of instances
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        try:
            with open(filename, newline="") as csvfile:
                list_objs = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_objs = [{k: int(v) for k, v in obj.items()}
                             for obj in list_objs]
                return [cls.create(**obj) for obj in list_objs]
        except FileNotFoundError:
            return []
