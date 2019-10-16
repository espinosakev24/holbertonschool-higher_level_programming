#!/usr/bin/python3
"""Module of read file"""


def read_file(filename=""):
    """read file function"""
    with open(filename, "r", encoding="utf-8") as fd:
        print(fd.read(), end="")
