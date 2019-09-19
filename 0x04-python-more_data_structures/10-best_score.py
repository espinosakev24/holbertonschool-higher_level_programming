#!/usr/bin/python3
def best_score(a_dictionary):
    num = []
    mx = 0
    idx = 0
    if not(a_dictionary):
        return None
    for a in a_dictionary:
        num.append(a_dictionary[a])
    mx = max(num)
    for key in a_dictionary:
        if a_dictionary[key] == mx:
            return key
    return None
