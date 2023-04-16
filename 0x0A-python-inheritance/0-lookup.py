#!/usr/bin/python3
"""Get attributes of a given class"""


def lookup(obj):
    """return array of attributes of a class
       args:
           obj: class object
    """
    return (dir(obj))
