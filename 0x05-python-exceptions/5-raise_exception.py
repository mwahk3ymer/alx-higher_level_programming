#!/usr/bin/python3

def raise_exception():
    try:
        value = "string"
        number = int(value)
    except ValueError:
        raise TypeError("Type conversion failed")
