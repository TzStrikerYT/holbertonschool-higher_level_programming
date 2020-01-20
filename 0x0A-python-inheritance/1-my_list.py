#!/usr/bin/python3
class MyList(list):
    """ Subclass to add methods to list class """
    def print_sorted(self):
        print(sorted(self))
