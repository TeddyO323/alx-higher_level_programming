#!/usr/bin/python3
'''
    Create two C functions that print some basic info
    about Python lists and Python bytes objects.
'''


def complex_delete(a_dictionary, value):

    for word in sorted(a_dictionary):
        if value == a_dictionary[word]:
            del a_dictionary[word]

    return a_dictionary
