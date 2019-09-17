#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        for a in matrix:
            for b in range(len(a)):
                if b != len(a) - 1:
                    print('{:d} '.format(a[b]), end="")
                else:
                    print('{:d}'.format(a[b]))
    else:
        print()
