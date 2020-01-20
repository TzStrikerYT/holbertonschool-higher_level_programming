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
