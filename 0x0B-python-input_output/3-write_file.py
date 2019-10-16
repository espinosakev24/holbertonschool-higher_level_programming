#!/usr/bin/python3
"""module of write a file"""


def write_file(filename="", text=""):
    """function write file"""
    with open(filename, "w+", encoding="utf-8") as fd:
        return fd.write(text)
