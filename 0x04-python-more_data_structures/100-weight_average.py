#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum, v = 0, 0
        for a, b in my_list:
            sum += a * b
            v += b
        return sum / v
    return 0
