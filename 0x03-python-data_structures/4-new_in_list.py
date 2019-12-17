#!/usr/bin/python3
def new_in_list(my_list, idx, element):
   if my_list:
      cp = my_list[:]
      if (idx < len(cp) and idx >= 0):
         cp[idx] = element
   return cp
