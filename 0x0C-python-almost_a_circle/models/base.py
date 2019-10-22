#!/usr/bin/python3
"""Module of Base Class"""
import json
import os.path


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
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """ Task --> 16 Json string to file """
    @classmethod
    def save_to_file(cls, list_objs):
        arch = cls.__name__ + ".json"
        with open(arch, "w", encoding="utf-8") as fd:
            if list_objs == []:
                fd.write('[]')
            new = []
            for a in list_objs:
                new.append(a.to_dictionary())
            content = cls.to_json_string(new)
            fd.write(content)

    """ Task --> 17 Json string to dict """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    """ Task --> 18 Dictionary to instance """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new = cls(1)
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    """ Task --> 19 return list of instances """
    @classmethod
    def load_from_file(cls):
        new_list = []
        new_content = ""
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, "r", encoding="utf-8") as fd:
                content = fd.read()
                new_content = cls.from_json_string(content)
                for a in new_content:
                    new_list.append(cls.create(**a))
            return new_list

    """ advance turtle task """
    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle

        sq = turtle.Turtle()
        sq.color('black')
        sq.shape('square')
