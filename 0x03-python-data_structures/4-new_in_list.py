#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces the element at a given index and return the
    modified copy of  list or copy of the original list on failure"""
    list_copy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return list_copy
    list_copy[idx] = element
    return list_copy
