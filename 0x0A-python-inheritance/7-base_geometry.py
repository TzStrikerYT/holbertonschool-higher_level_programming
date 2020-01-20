#!/usr/bin/python3
class BaseGeometry:
    """ Empty class """
    def __init__(self):
        pass

    def area(self):
        """ method no implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if is a integer and if is gretter than 0 or not """
        if (value.__class__ != int):
            raise TypeError("{:} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
