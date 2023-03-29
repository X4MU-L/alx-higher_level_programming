#!/usr/bin/python3

"""This Module contains a python class Square"""


class Square:
    """Square is a python class with a private size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square objects
        called on class instanciation
        Args:
            size (int): the size of the new square
        """

        self.size = size
        self.position = position

    def __str__(self):
        """Print the square with the # character."""
        str_ = ""
        if self.__size == 0:
            return ("\n")

        for i in range(0, self.position[1]):
            str_ += "\n"
        for i in range(0, self.__size):
            for j in range(0, self.position[0]):
                str_ += " "
            for k in range(0, self.size):
                str_ += "#"
            if i + 1 != self.__size:
                str_ += "\n"
        return (str_)

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, size):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """gets the area of the square"""

        return (self.size**2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.position[0])]
            [print("#", end="") for k in range(0, self.size)]
            print("")
