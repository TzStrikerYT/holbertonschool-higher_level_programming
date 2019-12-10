#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = ["Last digit of", "is", "and is greater than 5", "and is 0",
       "and is less than 6 and not 0"]
dig = number % 10 if number >= 0 else (abs(number) % 10) * -1
print(str[0], number, str[1], dig, str[2] if dig > 5 else str[3] if dig == 0
      else str[4])
