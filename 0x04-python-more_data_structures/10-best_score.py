#!/usr/bin/python3
'''
    Write a function that returns a key with the biggest integer value.
'''


def best_score(a_dictionary):

    bestScore = 0
    bestScore_name = ""

    if a_dictionary is None:
        return None

    if not a_dictionary:
        return None

    for key in a_dictionary:
        if a_dictionary[key] > bestScore:
            bestScore = a_dictionary[key]
            bestScore_name = key

    return bestScore_name
