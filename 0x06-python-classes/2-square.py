#!/usr/bin/python3
"""Defining a class Square"""

class Square:
    """Respresent a Square."""

    def __init(self, size):
        """Initilizing a new Square

        Args:
            size (int):The size of new square
        """
        #Validating size before initilization
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
