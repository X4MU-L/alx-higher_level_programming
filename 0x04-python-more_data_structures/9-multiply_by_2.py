#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    new_dict = a_dictionary.copy()
    for key in keys:
        new_dict[key] *= 2
    return (new_dict)
