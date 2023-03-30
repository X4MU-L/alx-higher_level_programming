#!/usr/bin/python3
def remove_char_at(str_, n):
    s = ""
    for i, c in enumerate(str_):
        if i == n:
            continue
        s += c
    return (s)
