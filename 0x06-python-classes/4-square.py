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

    """ intercept the write, read and delete of the attributes """
    @property
    def size(self):
        """ return value of size variable in the class """
        return self.__size

    """ setter intercepts when the atribute writes """
    @size.setter
    def size(self, value):
        """ sets size variable of square class instance """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
