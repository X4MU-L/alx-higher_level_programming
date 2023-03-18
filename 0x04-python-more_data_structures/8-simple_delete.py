#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key:
        try:
            del a_dictionary[key]
            return (a_dictionary)
        except KeyError:
            return (a_dictionary)
    return (a_dictionary)
