#!/usr/bin/python3
def islower(c):
    for a in range(97, 123):
        if ord(c) == ord(chr(a)):
            return True
    return False
