#!/usr/bin/python3
"""Creates a Rectangle class"""


class Rectangle:
    """A rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates a new Rectangle
        Args:
             width (int) the width of the rectangle
             height (int) the heighte of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            [print(str(self.print_symbol), end="")
             for k in range(self.__width)]
            if i + 1 != self.__height:
                print("")
        return ("")

    def __repr__(self):
        """returns a recreatable object of a rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """deletes instance of a rectangle"""
        if type(self).number_of_instances == 0:
            return
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """create a square from a rectangle class"""
        return cls(size, size)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Get the bigger area of a two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)

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
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
