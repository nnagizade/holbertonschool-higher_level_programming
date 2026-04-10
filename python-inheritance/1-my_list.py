#!/usr/bin/python3
"""
This module contains the MyList class.
"""


class MyList(list):
    """
    A class that inherits from the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
