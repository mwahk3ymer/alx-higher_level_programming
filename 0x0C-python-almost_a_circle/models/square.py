#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
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
            size (int): The size of the square ( and height).
            x (int, optional): The x-coordinate . Defaults to 0.
            y (int, optional): The y-coordinate . Defaults to 0.
            id (int, optional): The ID for the instance. D tone.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The new size value for both width and height.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: The str rep in the format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    def update(self, *args, **kwargs):
        """
        Update the Square attributes withder or keyworded arguments.

        Args:
            *args: Arguments in the order: id, size, x, y.
            **kwargs: Key-worded argumentnames and their values.
        """
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
