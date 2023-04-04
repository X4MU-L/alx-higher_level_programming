#!/usr/bin/python3

"""Module for matrix division"""


def matrix_divided(matrix, div):
    """Divide a matrix and return a matrix of it,s float division
       args:
            matrix: array of arrays of int/float
            div: int/float to divide each integer in matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or matrix is None or type(matrix) is not list:
        raise TypeError(error)

    if type(matrix[0]) is list and matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error)
    new_matrix = []
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(error)
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for num in matrix[i]:
            if type(num) not in [int, float]:
                raise TypeError(error)
            new_matrix[i].append(round(num / div, 2))

    return (new_matrix)
