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
    __init__(self, size=0):
        Constructs all the necessary attributes for the square object.
    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size : int, optional
            The size of the square's side (default is 0).

        Raises
        ------
        TypeError
            If the size is not an integer.
        ValueError
            If the size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.

        Returns
        -------
        int
            The area of the square.
        """

        return (self.__size ** 2)
