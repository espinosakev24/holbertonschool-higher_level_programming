#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def sq(num):
        return num * num
    new = []
    for a in matrix:
        new.append(list(map(sq, a)))
    return new
