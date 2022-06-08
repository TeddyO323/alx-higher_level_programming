#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newSet = set()
    for item in set_1:
        if (item in set_2) is False:
            newSet.add(item)
    for item in set_2:
        if (item in set_1) is False:
            newSet.add(item)
    return newSet
