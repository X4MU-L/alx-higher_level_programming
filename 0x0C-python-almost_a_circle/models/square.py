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
        """Get/set the width property"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes using a variable length of args
           *args:
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
           **kwargs: ony when args is not availble use the keywards to update
        """
        if args && len(args) != 0:
            i = 0
            for arg in args:
                if i = 0:
                    if arg is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i = 1:
                    self.size = arg
                elif i = 2:
                    self.x = arg
                elif i = 3:
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
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value