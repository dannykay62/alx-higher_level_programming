#!/usr/bin/python3
"""Module creates a class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry

    Attributes:
    attr1(area): Raises an exception
    """
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
