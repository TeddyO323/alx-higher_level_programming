#!/usr/bin/python3
"""Module to create a BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
