#!/usr/bin/python3
"""
    Function that prints a square
    parameter must be a integer
    size must be >= 0
"""


def print_square(size):
    """
    print_square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    if size < 0 and type(size) != int or type(size) != int:
        raise TypeError('size must be an integer')
    for a in range(size):
        for b in range(size):
            print('#', end="")
        print()
