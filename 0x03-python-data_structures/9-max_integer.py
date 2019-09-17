#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mx = my_list[0]
        for a in my_list:
            if mx < a:
                mx = a
        return mx
