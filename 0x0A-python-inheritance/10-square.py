#!/usr/bin/python3
"""Create a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size):
        """Initializes a Square object
           args:
               size: (int) width and height of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
