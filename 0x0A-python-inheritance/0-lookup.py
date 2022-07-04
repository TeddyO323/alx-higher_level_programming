#!/usr/bin/python3
"""Function to see attributes and methods of an object"""


def lookup(obj):
    """Search all attribute and methods that the object has
    Args:
      obj (object): object to search attributes
    """
    return list(dir(obj))
