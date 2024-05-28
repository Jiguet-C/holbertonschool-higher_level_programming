#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: The name of the file to read. Defaults to an empty str.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
