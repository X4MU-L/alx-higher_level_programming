#!/usr/bin/python3

"""This Module contains a python class Square"""
class Square:
    """Square is a python class with a private size attribute"""

    def __init__(self, size=0):
        """Initializes the square objects
        called on class instanciation
        Args:
            size (int): the size of the new square
        """

        self.size = size

    def __str__(self):
        """This function is called by the Print function
        Returns a string representation of the private attribute
        size"""

        return f"{{'_Square__size': {self.size}}}"

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """Sets the size property of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Gets and returns the area of the square object"""

        return (self.__size**2)
