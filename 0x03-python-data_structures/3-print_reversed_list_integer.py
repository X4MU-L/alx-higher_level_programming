#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integers one line at a time in reverse"""
    for i in my_list.reverse():
        print("{:d}".format(i))
