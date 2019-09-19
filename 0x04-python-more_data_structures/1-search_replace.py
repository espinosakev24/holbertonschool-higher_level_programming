#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = 0
    cpy = my_list[:]
    new = []
    for a in cpy:
        if a == search:
            del cpy[n]
            new.append(replace)
        new.append(cpy[n])
        n += 1
    return new
