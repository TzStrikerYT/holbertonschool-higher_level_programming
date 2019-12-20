#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = {key: _value for key, _value in a_dictionary.items()
         if _value == value}
    for k in a:
        a_dictionary.pop(k)
    return a_dictionary
