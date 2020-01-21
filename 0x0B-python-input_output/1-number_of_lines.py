#!/usr/bin/python3
def number_of_lines(filename=""):
    """ return total lines in the file """
    with open(filename, mode="r", encoding="utf-8") as o_file:
        return (len(o_file.readlines()))
