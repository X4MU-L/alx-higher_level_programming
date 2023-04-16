#!/usr/bin/python3
"""Create a Myint Class"""


class MyInt(int):
    """Define MyInt class"""

    def __eq__(self, value):
        """Changes == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Changes != operator with == behavior."""
        return self.real == value
