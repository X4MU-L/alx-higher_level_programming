#!/usr/bin/python3
"""Create a Pascal's Trinagle"""


def pascal_triangle(n):
    """Returns an array of pascals tringle of n
       Args:
           n: (integer) the amount of trainge to create
    """
    new = []
    if n > 0:
        for i in range(n):
            if i == 0:
                new.append([1])
                continue
            arr = []
            s = 0
            ind = i - 1
            for k in range(len(new[ind])):
                arr[len(arr):] = [s + new[ind][k]]
                s = new[ind][k]
            arr[len(arr):] = [1]
            new[len(new):] = [arr]
    return new
