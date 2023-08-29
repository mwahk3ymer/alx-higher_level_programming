#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Returns:
            None.
        """
        self.__size = size
