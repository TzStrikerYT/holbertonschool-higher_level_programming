#!/usr/bin/python3
def fizzbuzz():

    s = ["Fizz",
         "Buzz",
         "FizzBuzz"]
    for i in range(1, 101):
        print(s[2] if (i % 3) == 0 and (i % 5) == 0 else
              s[0] if (i % 3) == 0 else
              s[1] if (i % 5) == 0 else i, end=' ')
