#!/usr/bin/python3
"""
Class that inherits from list
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.

    This class provides additional functionality to sort and print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sort_list = super().copy()
        sort_list.sort()
        print(sort_list)
