#!/usr/bin/python3
def add_attribute(obj, value, name):
    """ Method that validate if it can ad sets an attributte """
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj,value, name)
    else:
        raise TypeError("can't add new attribute")
