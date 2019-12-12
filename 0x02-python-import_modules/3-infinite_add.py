#!/usr/bin/python3
from sys import argv


def main():
    add = 0
    for i argv[1:]:
        add += int(i)
    print("{:d".format(add))

if __name__ == "__main__":
    main()
