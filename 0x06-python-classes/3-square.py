#!/usr/bin/python3
class Square:
    """ Square class """
    def __init__(self, size=0):
        """ size of the square """
        if type(size) == int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ area of square :v """
        return self.__size ** 2
