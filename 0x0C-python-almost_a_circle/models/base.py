#!/usr/bin/python3
"""Create a Base Module"""


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
