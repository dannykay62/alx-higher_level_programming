#!/usr/bin/python3

"""Define a Python class MagicClass that does exactly the same as the following
Python bytecode provided."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of th new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not float and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """Return area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of MagicClass."""
        return (2 * math.pi * self.__radius)
