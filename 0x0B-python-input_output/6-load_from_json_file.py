#!/usr/bin/python3
"""
Contains the "undtion
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the JSON file to be read.
    :return: The Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
