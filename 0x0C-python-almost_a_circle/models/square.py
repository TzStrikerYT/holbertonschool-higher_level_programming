#!/usr/bin/python3
""" module for square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square that inherits rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns string info of the square """
        return "[{}] ({}) {}/{} - {}".\
            format(__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size of the square """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def updater(self, id=None, size=None, x=None, y=None):
        """ updates instance attribites from */**args """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ updates atribtes via no-kwrd and kwrd args """
        if args:
            self.updater(*args)
        elif kwargs:
            self.updater(**kwargs)

    def to_dictionary(self):
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
