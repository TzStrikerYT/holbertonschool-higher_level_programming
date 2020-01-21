#!/usr/bin/python3
class Student():
    """ class studentwith name and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns in json format """
        if attrs is None:
            return (self.__dict__)
        else:
            tmp = self.__dict__
            new = dict(([name, value] for name, value in tmp.items()
                        if name in attrs))
            return new
