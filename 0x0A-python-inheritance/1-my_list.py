#!/usr/bin/python3
"""Create a MyList class that inherits from a list"""



class MyList(list):
    """A class for new list that inherits list class"""

    def print_sorted(self):
        """prints a sorted version of a list"""
        print(sorted(self))
