#!/usr/bin/python3
class Rectangle:
    """ it defines a rectangle  """
    number_of_instances = 0
    print_symbol = "#"

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
        """ string representation of a rectangle with print symbol"""
        string = ''

        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                string += str(self.print_symbol * self.__width) + "\n"
            return string[:-1]

    def __repr__(self):
        """ string reoresentation of a rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ print message and delete the instance """
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger rectangle or if both are equal"""
        if (not isinstance(rect_1, Rectangle) or not isinstance(rect_2,
                                                                Rectangle)):
            raise TypeError("{:} must be an instance of Rectangle".format
                            ("rect_2" if isinstance(rect_1, Rectangle)else
                             "rect_1"))
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ return a square of length x width both """
        return cls(size, size)
