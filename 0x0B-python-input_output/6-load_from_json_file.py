#!/usr/bin/python3
"""Module creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
    filename (str): JSON file to create an object from
    """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
