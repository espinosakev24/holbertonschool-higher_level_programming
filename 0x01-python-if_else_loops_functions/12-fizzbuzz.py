#!/usr/bin/python3
def fizzbuzz():
    x = 101
    for a in range(1, x):
        if a != x:
            if a % 3 == 0 and a % 5 == 0:
                print("FizzBuzz, ", end="")
            elif a % 5 == 0:
                if not(a == 100):
                    print("Buzz, ", end="")
                else:
                    print("Buzz" end="")
            elif a % 3 == 0:
                print("Fizz, ", end="")
            else:
                print('{:d}, '.format(a), end="")
