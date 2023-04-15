#!/usr/bin/python3
"""Search and Append line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line to a text file if a word is found in the file
       args:
           filename: (str) name of file
           search_string: (str) the string to search for
           new_string: (str) the string to append to file
    """
    if filename:
        string = ""
        with open(filename, encoding="UTF-8") as f:
            for line in f:
                string += line
                if search_string in line:
                    string += new_string
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(string)
