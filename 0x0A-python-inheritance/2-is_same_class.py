#!/usr/bin/python3
"""check if same class"""


def is_same_class(obj, a_class):
    """checks if an object is same instance of a given class
       args:
           obj: (instance of a class) object to check
           a_class: (a class)
    """
    return (type(obj) == a_class)
