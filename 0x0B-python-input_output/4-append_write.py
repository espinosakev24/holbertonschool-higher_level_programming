#!/usr/bin/python3
"""module of write a file"""


def append_write(filename="", text=""):
    """function append write"""
    with open(filename, "a", encoding="utf-8") as fd:
        return fd.write(text)
