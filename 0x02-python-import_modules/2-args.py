#!/usr/bin/python3
import sys


def main():
    leng = len(sys.argv)
    print("{:d} argument{}".format(leng - 1, "s." if leng == 1 else
                                    (":" if leng == 2 else "s:")))
    a = 1
    for i in sys.argv[1:]:
        print("{:d}: {}".format(a, i))
        a = a + 1

if __name__ == "__main__":
    main()
