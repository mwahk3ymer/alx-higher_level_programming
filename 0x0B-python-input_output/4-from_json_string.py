#!/usr/bin/python3
"""
Contains the "to_json_string" fundtion
"""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.
    """
    return json.loads(my_str)
