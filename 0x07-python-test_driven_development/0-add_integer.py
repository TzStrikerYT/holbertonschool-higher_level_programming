#!/usr/bin/python3
"""
Doctests in python :D


"""


def add_integer(a, b=98):
    """ add 2 integers args are in a and b,
    if args are invalid type, the TypeError
    will be raised """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return int(a + b)
