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

    @property
    def width(self):
        """Get/set the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Get/Set the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/Set the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/Set the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
