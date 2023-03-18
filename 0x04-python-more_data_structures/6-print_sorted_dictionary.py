#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(dict.keys(a_dictionary))
    for key in sorted(keys):
        print(f"{key} : {a_dictionary[key]}")
