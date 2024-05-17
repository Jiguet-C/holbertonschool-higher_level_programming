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
        """Gets the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
            return ()

        position_y = 0
        while position_y < self.__position[1]:
            print("")
            position_y += 1

        size = 0
        while size < self.__size:
            print(" " * self.__position[0] + "#" * self.__size)
            size += 1
