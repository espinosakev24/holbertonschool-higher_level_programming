#!/usr/bin/pytho3
def print_reversed_list_integer(my_list=[]):
    for n in my_list[::-1]:
        print('{:d}'.format(n))