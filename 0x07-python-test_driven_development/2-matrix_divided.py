#!/usr/bin/python3
"""
    module with matrix divided function
    parameters - list of lists and int
    return new matrix divided
"""


def matrix_divided(matrix, div):
    """
    matrix_divided
    """
    s1 = 'matrix must be a matrix (list of lists) of integers/floats'
    s2 = 'division by zero'
    s3 = 'Each row of the matrix must have the same size'
    s4 = 'div must be a number'
    s5 = 'matrix must be a matrix (list of lists) of integers/floats'
    if len(matrix) == 0:
        raise TypeError(s1)

    if div == 0:
        raise ZeroDivisionError(s2)

    for length in matrix:
        if len(matrix[0]) != len(length):
            raise TypeError(s3)

    if type(div) is not int and type(div) is not float:
        raise TypeError(s4)

    for li in matrix:
        if not isinstance(li, list):
            raise TypeError(s5)
        for a in li:
            if type(a) is not int and type(a) is not float:
                raise TypeError(s6)
    new = []
    for a in range(len(matrix)):
        new.append(matrix[a].copy())
        for b in range(len(matrix[a])):
            new[a][b] = matrix[a][b] / div
            new[a][b] = round(new[a][b], 2)
    return new
