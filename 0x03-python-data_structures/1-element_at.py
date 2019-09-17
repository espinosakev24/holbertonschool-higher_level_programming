#!/usr/bin/python3
def element_at(my_list, idx):
    a = 0
    if not(idx < 0 or idx > len(my_list)):
        for n in my_list:
            if idx == a:
                return n
            a += 1
