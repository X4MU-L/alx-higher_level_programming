#!/usr/bin/python3
"""check if same class or inherited from same class"""


def is_kind_of_class(obj, a_class):
    """checks if an object is same or inherited from given class
       args:
           obj: (instance of a class) object to check
           a_class: (a class)
    """
    return (isinstance(obj, a_class)
