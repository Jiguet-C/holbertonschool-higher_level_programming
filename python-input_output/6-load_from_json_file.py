#!/usr/bin/python3
"""Module containing the function load_from_json_file"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the JSON file to read from.
    :return: The corresponding Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
