#!/usr/bin/python3
"""Module defines to_json_string function"""


import json


def from_json_string(my_str):
    """Returns JSON representative of object (string)
    Args:
    my_obj (str): object to return JSON representation of

    """
    return json.loads(my_str)
