#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_ = 0
    if my_list:
        my_list = set(my_list)
        for i in my_list:
            sum_ += i
        return (sum_)
    return (sum_)
