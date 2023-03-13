#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add the first two elements of 2 different tuples differently
    if any of the tuples first 2 elements are empty replace with 0"""
    tuple_a += (0,0)
    tuple_b += (0,0)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
