#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted([key for key in a_dictionary]):
        print("{}: {}".format(i, a_dictionary[i]))