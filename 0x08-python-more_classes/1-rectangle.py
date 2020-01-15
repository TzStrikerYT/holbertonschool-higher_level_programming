#!/usr/bin/python3
class Rectangle:
    """ it defines a rectangle  """
    def __init__(self, width=0, height=0):
        """ init atributes of the object rectangle """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ returns height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ stes height of the rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ returns widh of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ stes width of the rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
