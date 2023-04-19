#!/usr/bin/python3
"""Create a Square class that inherits from a Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square Object
           args:
               size: (int) the size of the square
               x: (int) the x attribute
               y: (int) the y attribute
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string representation of Rectangle attribute infos"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width))
