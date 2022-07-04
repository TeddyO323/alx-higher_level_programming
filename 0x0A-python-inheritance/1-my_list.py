#!/usr/bin/python3
"""Module to create a class inherit"""


class MyList(list):
    """This is the MyList class"""

    def print_sorted(self):
        """print the list in sort"""
        print(sorted(self))
