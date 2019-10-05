#!/usr/bin/python3
"""
    Module with add_integer function
    Function that adds two numbers
    This module only has one function
"""


def add_integer(a, b=98):
    """
    add_integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if a > 1e400:
        raise OverflowError
    if a > 1e400:
        raise OverflowError
    c = a + b
    return int(c)
