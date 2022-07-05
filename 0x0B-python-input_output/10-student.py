#!/usr/bin/python3
"""
Student Class json object
"""


class Student:

    """
    Represent Student Object
    """
    def __init__(self, first_name, last_name, age):

        """
        initialization
        Args:
            first_name: first_name
            last_name: last_name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """
        Convert to json
        Args:
            attrs: attributes
        """
        result = {}
        if attrs is None:
            return self.__dict__
        else:
            for s in attrs:
                if s in self.__dict__:
                    result[s] = self.__dict__[s]
        return result
