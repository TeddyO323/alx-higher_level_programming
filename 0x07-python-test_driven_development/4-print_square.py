#!/usr/bin/python3
"""Module has function print_square
"""


def print_square(size):
    """This is the print_square function
    Print a square with # symbols
    Args:
       size (int positive): Square's size
    """
    if (type(size) != int) or (type(size) == float and size < 0):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
