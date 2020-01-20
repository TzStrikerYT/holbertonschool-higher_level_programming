#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle that inherits from basegeometry """
    def __init__(self, width, height):
        """ init atrubuttes of the class """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of arectangle """
        return self.__width * self.__height

    def __str__(self):
        """ prints a holberton check format """
        return "[{}] {:d}/{:d}".format(__class__.__name__, self.__width,
                                       self.__height)


class Square(Rectangle):
    """ class that inherit rectangle class """
    def __init__(self, size):
        """ init the atributtes of square class """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
