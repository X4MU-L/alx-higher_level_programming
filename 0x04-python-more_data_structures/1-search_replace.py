#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        my_list = [replace if x == search else x for x in my_list]
        return my_list
    return my_list
