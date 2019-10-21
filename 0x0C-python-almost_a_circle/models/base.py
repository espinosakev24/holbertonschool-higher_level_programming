#!/usr/bin/python3
"""Module of Base Class"""
import json

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

    """ Task --> 15 Dict to Json string """
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
           return json.dumps(list_dictionaries)

    """ Task --> 16 Json string to file """
    @classmethod
    def save_to_file(cls, list_objs):
        arch = cls.__name__ + ".json"
        new = []
        for a in list_objs:
            new.append(a.to_dictionary())
        content = cls.to_json_string(new)
        with open(arch, "w", encoding="utf-8") as fd:
           return fd.write(content)

    """ Task --> 17 Json string to dict """
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    """ Task --> 18 Dictionary to instance """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new = cls(1, 0, 0)
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)
        new.update(**dictionary)
        return new
        
