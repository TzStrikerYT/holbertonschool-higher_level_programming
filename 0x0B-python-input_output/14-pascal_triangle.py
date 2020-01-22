#!/usr/bin/python3
def pascal_triangle(n):
    p_list = []

    if n <= 0:
        return pascal_list

    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                p_list.append([1])
            elif i == j:
                p_list[i].append(1)
            else:
                p_list[i].append(p_list[i - 1][j] + p_list[i - 1][j - 1])
    return p_list
