#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not(idx < 0 or len(my_list) < idx):
       del my_list[idx]
       return my_list
    else:
        return my_list
