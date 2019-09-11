#!/usr/bin/python3
def uppercase(str):
    n = 0
    for a in range(len(str)):
        if ord(str[n]) >= 61 and ord(str[n]) <= 122:
            print('{}'.format(chr(ord(str[n]) - 32)), end="")
            n += 1
    print()
