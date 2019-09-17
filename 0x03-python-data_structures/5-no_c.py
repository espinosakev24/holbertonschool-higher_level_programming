#!/usr/bin/python3
def no_c(my_string):
    a = 0
    string = ""
    for n in my_string:
        if n == 'C' or n == 'c':
            continue
        string = string + n
        a += 1
    return string
