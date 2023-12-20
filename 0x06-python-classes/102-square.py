#!/usr/bin/python3

"""This module contains the definition of a Square"""


class Square:
    """A Square class will be used to create a square shape."""

    def __init__(self, size=0):
        """Intantiates a square object.

        Args:
            size (int): the size of the square
        """
        self.size = size

    def area(self):
        """Computes the area of a square."""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of this square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of this square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """Compares squares equality.

        Args:
            other: (Square)
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares squares equality.

        Args:
            other: (Square)
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square is greater than the other.

        Args:
            other: (Square)
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equals
        to the other.

        Args:
            other: (Square)
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if this square is lesser than the other.

        Args:
            other: (Square)
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is lesser than or equals
        to the other.

        Args:
            other: (Square)
        """
        return self.area() <= other.area()
