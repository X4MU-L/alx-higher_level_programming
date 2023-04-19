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

    @property
    def size(self):
        """Get/set the width/height property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes using a variable length of args
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represent size attribute
                - 5th argument represents x attribute
                - 4th argument represents y attribute
            **kwargs dict: key/value pairs of attributes
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return a dictionary representaion of Square object"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
