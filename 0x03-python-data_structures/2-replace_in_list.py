#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces the element at a given index and return the
    modified list or original list on failure"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
