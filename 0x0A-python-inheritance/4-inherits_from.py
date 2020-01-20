#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ returns true if the object is an instance of a cla"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
