#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Instanciates a new Student object
        Args:
            first_name: (string) first name of the student.
            last_name: (string) last name of the student.
            age: (integer) age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a json/dict repsentation of an object"""
        return self.__dict__
