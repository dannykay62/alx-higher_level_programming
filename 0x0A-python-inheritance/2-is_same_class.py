#!/usr/bin/python3
"""Function compares two objects for type"""


def is_same_class(obj, a_class):
    """Returns True if the object is excatly an instance of the
    specified class"""
    return type(obj) == a_class
