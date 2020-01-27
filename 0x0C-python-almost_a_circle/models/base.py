#!/usr/bin/python3
""" Modules """
from json import dumps, loads


class Base:
    """ Base class of the others class in the project """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ encode to json """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ decode from json """
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves JSON object to file """
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), mode="w",
                  encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """ instance loader """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            n = Rectangle(1, 1)
        if cls is Square:
            n = Square(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """ load strings from file """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, mode="r", encoding="utf-8") as f:
            return [cls.create(**i) for i in cls.from_json_string(f.read())]
