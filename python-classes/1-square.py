#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    A class used to represent a square.

    Attributes
    ----------
    size : int
        The size of the square's side.

    Methods
    -------
    __init__(self, size):
        Constructs all the necessary attributes for the square object.
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size : int
            The size of the square's side.
        """

        self.__size = size
