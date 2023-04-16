#!/usr/bin/python3
"""Create a Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class"""

    def __init__(self, width, height):
        """Initializes a Rectangle object
           args:
               width: (int) width of the Rectangle
               height: (int) height of the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
