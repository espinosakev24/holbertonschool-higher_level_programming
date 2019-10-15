#!/usr/bin/python3
"""Module of is_same_class"""


def is_same_class(obj, a_class):
    """is same class function"""
    if type(obj) is a_class:
        return True
    else:
        return False
