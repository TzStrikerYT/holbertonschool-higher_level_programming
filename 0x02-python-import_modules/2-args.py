#!/usr/bin/python3
import sys

def main():
    length = len(sys.argv)
    print("{:d]: argument{:}".format(l - 1, "." if l == 1 else
                                     (":" if l == 2 else "s:")))
    argp = 1
    for i  in sys.argv[1:]:
        print("{:d}: {}".format(argp, i))
        argp =+ 1

if __name__ == "__main__":
    main()
