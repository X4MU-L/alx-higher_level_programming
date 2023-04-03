#!/usr/bin/python3
"""Creates a Rectangle class"""


class Rectangle:
    """A rectangle object"""

    def __init__(self, width=0, height=0):
        """Instantiates a new Rectangle
        Args:
             width (int) the width of the rectangle
             height (int) the heighte of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width property of a new rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height property of a new rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of a rectangle object"""
        return (2 * (self.__width + self.__height))