#!/usr/bin/python3
""" modules for class rectangle """
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherits base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init attributes for rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ width of the rectangle """
        self.integerValidator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ width of the rectangle """
        self.integerValidator("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ width of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ value in x in the rectangle """
        self.integerValidator("x", value)
        self.__x = value

    @property
    def y(self):
        """ value in y in the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ value in y in the rectangle """
        self.integerValidator("y", value)
        self.__y = value

    def integerValidator(self, name, value, xy=True):
        """ validates if integer value or not and validates 0 values """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if xy and value < 0:
            """ x and y validator """
            raise ValueError("{} must be >= 0".format(name))
        if not xy and value <= 0:
            """ width and height validator """
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Displays rectangle visual representation """
        final = "\n" * self.y + \
                (" " * self.x + "#" * self.__width + "\n") * self.__height
        print(final, end="")

    def __str__(self):
        """ Returns info of the rectangle """
        return "[{}] ({}) {}/{} - {}/{}".\
            format(__class__.__name__, self.id, self.__x, self.__y,
                   self.__width, self.height)

    def updater(self, id=None, width=None, height=None, x=None, y=None):
        """ updates instance attribites from */**args """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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
        """ encode to JSON """
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
