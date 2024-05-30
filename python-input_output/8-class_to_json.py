#!/usr/bin/python3
"""
Defines a function that converts an object's attributes to a dictionary
suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of an object's attributes
    for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary containing the attributes of the object.
    """
    json_obj = vars(obj)
    return json_obj
