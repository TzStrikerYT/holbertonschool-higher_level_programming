#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ read nlines in the file """
    if nb_lines < 0:
        nb_lines = 0
    with open(filename, mode='r', encoding="utf-8") as o_file:
        for i, line in enumerate(o_file):
            if (nb_lines and nb_lines == i):
                break
            print(line, end="")
        o_file.close()
