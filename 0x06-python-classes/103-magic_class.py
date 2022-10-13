#!/usr/bin/python3
"""Definse a MagicClasss"""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a circle.

        Args:
            radius (float or int): The radiu of the new MagicClass

        """
        self.__radius = 0
        if type(radius) is  not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass"""
        return (sef.radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)


