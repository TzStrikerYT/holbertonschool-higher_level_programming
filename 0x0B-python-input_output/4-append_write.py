#!/usr/bin/python3
def append_write(filename="", text=""):
    """ append a string text in a file """
    chars = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        chars += f.write(text)
        f.close()
    return chars
