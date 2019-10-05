#!/usr/bin/python3
"""
    
"""

def matrix_divided(matrix, div):
    if len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for length in matrix:
        if len(matrix[0]) != len(length):
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    for li in matrix:
        if not isinstance(li, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for a in li:
            if type(a) is not int and type(a) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new = []
    for a in range(len(matrix)):
        new.append(matrix[a].copy())
        for b in range(len(matrix[a])):
            new[a][b] = matrix[a][b] / div
            new[a][b] = round(new[a][b], 2)
    return new
