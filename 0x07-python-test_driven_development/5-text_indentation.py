#!/usr/bin/python3
"""module for text_indentation"""


def text_indentation(text):
    """Indent text using [., ?, :]
       args:
           text: (string) text to indent
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    text_len = len(text)
    while i < text_len:
        while text[i] == " ":
            i += 1
            if i == text_len:
                return
        indent = ""
        while text[i] not in [".", "?", ":"] and i < text_len - 1:
            indent += text[i]
            i += 1
        indent += text[i]
        if text[i] in [".","?", ":"]:
            print(indent)
            print("")
        else:
            print(indent, end="")
        i += 1
