#!/usr/bin/python3
def max_integer(my_list=[]):
    """Get the max integer from a list"""
    if my_list:
        len_ = len(my_list) - 1
        i = 0
        while (i < len_):
            for k in range(len_):
                if my_list[k] > my_list[k + 1]:
                    temp = my_list[k]
                    my_list[k] = my_list[k + 1]
                    my_list[k + 1] = temp
            i += 1
        return my_list[-1]
