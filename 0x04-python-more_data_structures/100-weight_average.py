#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        moving_total = 0
        weight_total = 0
        for i in my_list:
            a, b = i
            moving_total = moving_total + (a * b)
            weight_total += b
        return (moving_total / weight_total)
    return (0)
