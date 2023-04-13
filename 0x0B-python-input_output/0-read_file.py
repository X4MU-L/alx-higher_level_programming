#!/usr/bin/python3

"""Read File Module"""


def read_file(filename=""):
    """Read and prints all the content of file
       args:
           filename - (strings) the name of the file to open
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
