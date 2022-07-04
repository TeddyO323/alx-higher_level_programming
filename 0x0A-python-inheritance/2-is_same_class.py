#!/usr/bin/python3
"""Module have a function"""


def is_same_class(obj, a_class):
    """This is the is_same_class method
    Is to verify is an object is equal a class
    Args:
       obj (object): object to compare
       a_class (class): Class to compare
    Returns:
       True: Equals classes
       False: Differents classes
    """
    return type(obj) == a_class
