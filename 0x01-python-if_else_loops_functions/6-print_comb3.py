#!/usr/bin/python3
for i in range(0, 10):
        for j in range(i + 1, 10):
                print("{:d}{:d}, ".format(i, j) if i < 8
                      else "{:d}{:d}\n".format(i, j), end="")
