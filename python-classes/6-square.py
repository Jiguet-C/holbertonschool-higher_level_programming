#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """A class used to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructs all the necessary attributes for the square object."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the size of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        size = 0
        while size < self.__size:
            print(" " * self.position[0] + "#" * self.__size)
            size += 1
