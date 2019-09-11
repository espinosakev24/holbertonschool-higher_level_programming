#!/usr/bin/python3
for a in reversed(range(97, 123)):
    if a % 10 == 0:
        a = chr(a)
    elif a % 10 != 0:
        a = chr(a - 32)
    print('{}'.format(a), end="")
