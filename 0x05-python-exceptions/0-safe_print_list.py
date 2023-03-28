#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    len_ = 0
    for i in range(x):
        try:
            len_ += 1
            print(my_list[i], end="")
        except IndexError:
            print()
            return (i)
    print()
    return (len_)
