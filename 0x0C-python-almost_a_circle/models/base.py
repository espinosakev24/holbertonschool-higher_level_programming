#!/usr/bin/python3
"""Module of Base Class"""


class Base:

    """Clase Base"""

    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
