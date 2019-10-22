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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ task --> advanced 1
        """
        arch = cls.__name__ + ".csv"
        with open(arch, "w", encoding="utf-8") as fd:
            if list_objs == []:
                fd.write('[]')
            new = []
            for a in list_objs:
                new.append(a.to_dictionary())
            content = cls.to_json_string(new)
            fd.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """ task --> advanced 1
        """
        new_list = []
        new_content = ""
        file_name = cls.__name__ + ".csv"
        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, "r", encoding="utf-8") as fd:
                content = fd.read()
                new_content = cls.from_json_string(content)
                for a in new_content:
                    new_list.append(cls.create(**a))
            return new_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ advance turtle task """
        import turtle

        sq = turtle.Turtle()
        sq.shape('square')
        sq.speed(1)
        a = list_rectangles[0]
        sq.color('green')
        for a in list_rectangles:
            sq.penup()
            sq.forward(a.x)
            sq.left(90)
            sq.forward(a.y)
            sq.right(90)
            sq.pendown()
            sq.forward(a.width)
            sq.left(90)
            sq.forward(a.height)
            sq.left(90)
            sq.forward(a.width)
            sq.left(90)
            sq.forward(a.height)
            sq.left(90)
            """back to the origin"""
            sq.penup()
            sq.right(180)
            sq.forward(a.x)
            sq.left(90)
            sq.forward(a.y)
            sq.left(90)
            sq.pendown()
        sq.color('blue')
        for b in list_squares:
            sq.penup()
            sq.forward(b.x)
            sq.left(90)
            sq.forward(b.y)
            sq.right(90)
            sq.pendown()
            sq.forward(b.width)
            sq.left(90)
            sq.forward(b.width)
            sq.left(90)
            sq.forward(b.width)
            sq.left(90)
            sq.forward(b.width)
            sq.left(90)
            """back to the origin"""
            sq.penup()
            sq.right(180)
            sq.forward(b.x)
            sq.left(90)
            sq.forward(b.y)
            sq.left(90)
            sq.pendown()
