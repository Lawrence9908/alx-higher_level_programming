#!/usr/bin/python3
"""Represent a class Square"""
class Square:

    def __init__(self, size=0):
        """Initialize a new Sqaure

        Args:
            size (int): The size of new Sqaure

        """
        self.size = size


    @property
    def size(self):
        """set the currect size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(valiue, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__size = value

    def area(self):
        """Reteun the current of the square"""
        return (self.__size * self.__size)

