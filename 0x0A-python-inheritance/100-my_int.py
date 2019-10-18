#!/usr/bin/python3
"""module of my int"""


class MyInt(int):
    def __eq__(self, other):
        return type(self) == int(other)

    def __ne__(self, other):
        return type(self) != int(other)
