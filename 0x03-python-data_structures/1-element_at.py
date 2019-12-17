#!/usr/bin/python3
def element_at(my_list, idx):

    l = len(my_list)

    if (idx >= l and idx < 0):
        return my_list[idx]
    else:
        return None
