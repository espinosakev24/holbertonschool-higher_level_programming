#!/usr/bin/python3
def remove_char_at(str, n):
    a = 0
    new = ""
    if n < 0:
        return str
    if not(n > len(str)):
        str_del = list(str)
        del str_del[n]
        for i in str_del:
            new = new + str_del[a]
            a += 1
        return new
    else:
        return str
