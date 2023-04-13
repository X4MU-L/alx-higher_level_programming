#!/usr/bin/python3
"""Append function Module"""


def append_write(filename="", text=""):
    """Append a given string to a file and return the number of
       charaters written
       Args:
            filename: (strings) file to write strings
            text: (strings) the strings to append into file
    """
    with open(filename, "a") as f:
        return (f.write(text))
