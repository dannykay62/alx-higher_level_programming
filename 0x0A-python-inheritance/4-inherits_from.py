#!/usr/bin/python3

"""Module defines nherits_from function"""


def inherits_from(obj, a_class):
    """returns True or False based on inheritance"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
