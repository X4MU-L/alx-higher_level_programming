#!/usr/bin/python3
"""check if same class or inherited from same class"""


def inherits_from(obj, a_class):
    """checks if an object is same or inherited from given class
       args:
           obj: (instance of a class) object to check
           a_class: (a class)
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
