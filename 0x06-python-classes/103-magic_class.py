#!/usr/bin/python3
"""
This module defines the MagicClass for circle calculations.

This module contains the MagicClass,methods for calculating
the area and circumference of a circle based on its radius.
"""

import math


class MagicClass:
    """
    A class for circle calculations.

    """

    def __init__(self, radius=0):
        """
        Initialize MagicClass with a radius.

        Args:
            radius (int or float): The radius of the circle (default is 0).

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
