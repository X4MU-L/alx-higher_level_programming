#!/usr/bin/python3
"""Write function Module"""


def write_file(filename="", text=""):
    """Writes a given string to a file and return the number of
       charaters written
       Args:
            filename: (strings) file to write strings
            text: (strings) the strings to write into file
    """
    with open(filename, "w") as f:
        return (f.write(text))
