#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of
    characters added.

    :param filename: The name of the file to append to. Defaults to an empty
    string.
    :param text: The string to append. Defaults to an empty string.
    :return: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
