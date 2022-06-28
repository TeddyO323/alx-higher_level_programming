#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is the test class
    3 Test to the function max_integer
    """

    def test_lists(self):
        """Test_lists function
        lists with positive numbers
        """
        list = []
        self.assertEqual(max_integer(list), None)

        list = [1, 2, 3]
        self.assertEqual(max_integer(list), 3)

        list = [86, 98, 120, 0]
        self.assertEqual(max_integer(list), 120)

    def test_lists_negatives(self):
        """tests_lists_negatives function
        lists with negative numbers
        """
        list = [-3, -8, 10, 9]
        self.assertEqual(max_integer(list), 10)

        list = [-1]
        self.assertEqual(max_integer(list), -1)

    def test_errors(self):
        """Tests_errors
        The common errors that happens in specific cases
        """
        list = None
        self.assertRaises(TypeError, max_integer, list)

        list = ["Hello", 2, 3]
        self.assertRaises(TypeError, max_integer, list)


if __name__ == '__main__':
    unittest.main()
