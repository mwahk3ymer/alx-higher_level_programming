#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (float or int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        Returns:
            None.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.

        Returns:
            None.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two Square instances are equal in terms of area.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two Square instances are not equal in terms of area.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if one Square instance has a larger area than the other.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if self's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one Square instance has a larger or equal area than the other.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if self's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if one Square instance has a smaller area than the other.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if self's area is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if one Square instance has a smaller or equal area than the other.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if self's area is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()
