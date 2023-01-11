#!/usr/bin/python3
"""Module defines to_json_string function"""


import json


def to_json_string(my_obj):
    """Return JSON representative of an object (string)
    Args:
    my_obj (str): object to returns JSON representation of
    """
    return json.dumps(my_obj)
