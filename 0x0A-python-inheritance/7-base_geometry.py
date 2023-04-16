#!/usr/bin/python3
"""Create a Geometry class"""


class BaseGeometry:
    """Define a BaseGeometry class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
