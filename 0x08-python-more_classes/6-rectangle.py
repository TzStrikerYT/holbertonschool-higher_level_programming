#!/usr/bin/python3
class Rectangle:
    """ it defines a rectangle  """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ init atributes of the object rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimetter of a rectangle """
        per = 0

        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = self.__width * 2 + self.__height * 2

        return per

    def __str__(self):
        """ string representation of a rectangle """
        string = ''

        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                string += str("#" * self.__width) + "\n"
            return string[:-1]

    def __repr__(self):
        """ string reoresentation of a rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ print message and delete the instance """
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")
