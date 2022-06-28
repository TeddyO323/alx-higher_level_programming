#!/usr/bin/python3
"""Module has a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """This is say_my_name function
    Prints the name of a person
    Args:
       first_name (str): first name of the person
       last_name (str): last name of the person
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
