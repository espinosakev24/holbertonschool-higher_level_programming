#!/usr/bin/python3
b = 0
x = 10
for n in range(x):
    for a in range(10):
        if b == x - 1 and a == x - 1:
            print('{:d}{:d}'.format(b, a))
        else:
            print('{:d}{:d}, '.format(b, a), end="")
    b += 1
