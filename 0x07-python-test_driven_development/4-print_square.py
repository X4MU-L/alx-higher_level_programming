#!/usr/bin/python3
"""This module is for print_square"""


def print_square(size):
    """Prints a square of given size using #
       args:
           size: int/float
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#", end="")
        print("")
