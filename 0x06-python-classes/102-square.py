#!/usr/bin/python3
"""Define a class Square"""

class Sqaure:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new Square
        
        Args:
            size (int) : The size of new Square
        """
        self.size = size

    @property
    def size(sef):
        """set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current are of the square"""
        return (self.__size * self.__size)

    def __ne__(self, another):
        """Define the not equal (!=) comparison to a square"""
        return self.area() != another.area()

    def __eq__(self, another):
        """Define the equal to (==) comparision to a Square."""
        return self.area() == another.area()

    def __lt__(self, another):
        """Define the less than (<) comparison to a Square."""
        return self.area() < another.area()

    def __ge__(self, another):
        """Define the greator that or equal (>=) compmarison to a Square."""
        return self.area() >= another.area()
    
    def __le__(self, another):
        """Define the less than or equal (<=) comparison to a Square."""
        return self.area() <= another.area()

    def __gt__(self, another):
        """Define the greater than (>) comparison to a Square."""
        return self.area() > another.area()

