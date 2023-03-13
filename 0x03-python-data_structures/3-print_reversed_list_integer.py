#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integers one line at a time in reverse"""
    my_list = my_list[::-1]
    if len(my_list) == 0:
        print()
        return
    for i in my_list:
        print("{:d}".format(i))
