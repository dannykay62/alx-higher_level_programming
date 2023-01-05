#!/usr/bin/python3
# 1-rectangle.py
"""Defines a class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectang;e.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the triangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """Get/set the height of the triangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
