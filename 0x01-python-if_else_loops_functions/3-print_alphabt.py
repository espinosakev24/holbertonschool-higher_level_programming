#!/usr/bin/python3
for n in range(0x61, 123):
    if n == 0x71:
        continue
    elif n == 101:
        continue
    print('{:s}'.format(chr(n)), end="")
