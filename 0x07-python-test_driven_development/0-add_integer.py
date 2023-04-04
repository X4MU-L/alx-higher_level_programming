#!/usr/bin/python3

"""
This module create s function to add integers
>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Function that adds two integers or floats

       args:
            a (int) or (float) to add
            b (int) or (float) to add
       returns:
            the addition of a and b
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return (a + b)
