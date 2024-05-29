#!/usr/bin/python3
"""Module containing the function to_json_string"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The object to be serialized to JSON.
    :return: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
