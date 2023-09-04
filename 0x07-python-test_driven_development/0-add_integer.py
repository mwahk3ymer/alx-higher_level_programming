#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98 if not provided.
    
    Returns:
        int: The sum of a and b, casted to an integer.
    
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("b must be an integer")
    
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    # Calculate and return the sum as an integer
    result = a + b
    return int(result)
