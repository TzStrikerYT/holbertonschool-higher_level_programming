#!/usr/bin/python3
def read_file(filename=""):
    """ reads text file """
    with open(filename, mode="r", encoding="utf-8") as o_file:
        print(o_file.read(), end="")
        o_file.close()
