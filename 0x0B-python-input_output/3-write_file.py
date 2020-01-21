#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes string to file and returns number of characters containing """
    chars = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        chars += f.write(text)
        f.close()
    return chars
