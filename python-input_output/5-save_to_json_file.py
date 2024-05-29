#!/usr/bin/python3
"""Module containing the function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    :param my_obj: The object to be serialized to JSON and written to the file.
    :param filename: The name of the file to write the JSON string to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
