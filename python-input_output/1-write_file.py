#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters.

    :param filename: The name of the file to write to. Defaults to an empty
    string.
    :param text: The string to write. Defaults to an empty string.
    :return: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
