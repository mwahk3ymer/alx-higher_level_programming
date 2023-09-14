#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectngle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the squaoth width and height).
            x (int, optional): The ate of the square. Defaults to 0.
            y (int, optional): The y-coordinate ore. Defaults to 0.
            id (int, optional): The ID for the instance. Dene.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: The string representation in (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
