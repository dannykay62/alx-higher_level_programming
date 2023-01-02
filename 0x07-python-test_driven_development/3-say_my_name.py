#!/usr/bin/python3

# 3-say_my_name.py

"""Defines a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed.
    Raises:
        TypeError: If either of the first_name or last_name is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TyperError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
