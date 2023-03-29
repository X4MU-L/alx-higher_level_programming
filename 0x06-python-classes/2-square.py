#!/usr/bin/python3

"""This Module contains a python class Square"""
class Square:
    """Square is a python class with a private size attribute"""

    def __init__(self, size=0):
        """Initializes the square objects
        called on class instanciation"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __str__(self):
        """This function is called by the Print function
        Returns a string representation of the private attribute
        size"""

        return f"{{'_Square__size': {self.size}}}"
