#!/usr/bin/python3
"""Module for function that adds 2 integers or floats
"""


def add_integer(a, b=98):
    """This is the add_integer function
    Is to add 2 integers/floats
    Args:
      a (int or float): first number
      b (int or float): second number
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
