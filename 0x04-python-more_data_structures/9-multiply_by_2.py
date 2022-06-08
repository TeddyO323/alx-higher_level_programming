#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for item in copy:
        copy[item] = a_dictionary.get(item) * 2
    return copy
