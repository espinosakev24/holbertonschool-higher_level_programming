#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = 0
    new_list = my_list[:]
    if idx >= len(my_list) or idx < 0:
        return new_list
    else:
        for n in new_list:
            if idx == a:
                new_list[a] = element
                return new_list
            a += 1
