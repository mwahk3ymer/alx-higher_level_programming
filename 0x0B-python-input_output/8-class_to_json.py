#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""



def class_to_json(obj):
    """
    Converts an instance of r JSON serialization.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("obj must be an instance of a Class")

    # Get the dictionary representation of the object's attributes
    obj_dict = obj.__dict__

    # Filter the dictionary to include only serializable data types
    serializable_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (int, str, bool, list, dict)):
            serializable_dict[key] = value

    return serializable_dict
