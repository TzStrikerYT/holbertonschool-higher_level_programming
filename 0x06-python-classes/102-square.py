#!/usr/bin/python3
class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ size of the square and position """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ returns position variable of square class instance """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets position variable of square class instance """
        if (type(value[0]) != int or type(value[1]) != int or
            type(value) != tuple or len(value) != 2 or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ area of square :v """
        return self.__size ** 2

    def my_print(self):
        """ prints a square of # """
        if self.__size == 0:
            print()
        else:
            if (self.__position):
                for i in range(self.__position[1]):
                    print()
                for i in range(self.__size):
                    print(' ' * self.__position[0], end="")
                    print('#' * self.size)
            else:
                for i in range(self.__size):
                    print('#' * self.__size)

    def __str__(self):
        """ converts to string """
        string = ""
        if self.__size != 0:
            if (self.__position):
                for i in range(self.__position[1]):
                    string += '\n'
                for i in range(self.__size):
                    string += str(" " * self.__position[0])
                    string += str('#' * self.size + '\n')
                string = string[:-1]
            else:
                for i in range(self.__size):
                    string *= str(('#' * self.__size) + '\n')
                string = string[:-1]
        return string

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size
