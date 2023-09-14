#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinatefaults to 0.
            y (int, optional): The y-coordinate Defaults to 0.
            id (int, optional): The ID for the instance. Defaults to None.
        """
        super().__init__(id)  # Call the constructor of the Base class

        # Private attributes with getters and setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method for height.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter method for x-coordinate.
        """
        return self.__x

    @property
    def y(self):
        """
        Getter method for y-coordinate.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): The new width value.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): The new height value.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter method for x-coordinate.

        Args:
            value (int): The new x-coordinate value.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter method for y-coordinate.

        Args:
            value (int): The new y-coordinate value.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle instance.

        Returns:
            int: The area value.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance using '#' characters to stdout.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        return a str rep of rectangle insatnce
        """
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """
        update rectangle attributes
        """
        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle instance.

        Returns:
            dict: A dic containing att id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
