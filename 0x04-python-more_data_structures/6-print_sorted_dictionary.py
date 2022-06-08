#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # keys = a_dictionary.keys()
    # print(a_dictionary.get("language"))
    list = sorted(a_dictionary)
    for item in list:
        print("{}:".format(item), a_dictionary.get(item))
