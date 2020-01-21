#!/usr/bin/python3

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class that inherit rectangle class """
    def __init__(self, size):
        """ init the atributtes of square class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
