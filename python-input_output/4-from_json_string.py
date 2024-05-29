#!/usr/bin/python3
"""Module containing the function from_json_string"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to deserialize.
    :return: The corresponding Python object.
    """
    return json.loads(my_str)
