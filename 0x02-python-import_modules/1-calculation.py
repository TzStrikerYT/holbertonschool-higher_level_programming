#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    sign = ["+", "-", "*", "/"]
    opc = {0: add, 1: sub, 2: mul, 3: div}
    for i in opc:
        print("{:d} {:} {:d} = {:d}".format(a, sign[i], b, opc[i](a, b)))

if __name__ == "__main__":
    main()
