#!/usr/bin/python3
"""Module of inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from function"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
