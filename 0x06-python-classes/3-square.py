#!/usr/bin/python3
"""Defines a square classs"""


class Square:
    """Defines a square class"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must ne an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of new square"""
        return (self.__size * self.size)
