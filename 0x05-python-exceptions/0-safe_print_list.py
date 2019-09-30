#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        for a in range(x):
            print('{}'.format(my_list[a]), end="")
            idx += 1
    except IndexError:
        pass
    print()
    return idx
