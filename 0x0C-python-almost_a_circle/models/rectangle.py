#!/usr/bin/python3
"""Create a Rectangle class inherit from Base"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle Object
           args:
               width: (int) the width of the Rectangle
               height: (int) the height of the Rectangle
               y: (int) y attribute
               x: (int) x attribute
               id: (any) the id of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """return a string representation of Rectangle attribute infos"""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width, self.height))

    @property
    def width(self):
        """Get/set the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/Set the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/Set the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get the area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the # representation of Rectangle"""
        [print("") for x in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            [print("#", end="" if k + 1 != self.__width else "\n")
             for k in range(self.__width)]
