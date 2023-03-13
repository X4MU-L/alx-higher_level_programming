#!/usr/bin/python3
def no_c(my_string):
    """Print a list of integers one line at a time in reverse"""
    if my_string:
        new_str = ""
        for c in my_string:
            if c not in "cC":
                new_str += c
        return new_str
    return my_string
