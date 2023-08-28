#!/usr/bin/python3

from sys import exc_info, stderr

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=stderr)
        return None

# Example functions
def divide(a, b):
    return a / b

def concatenate(a, b):
    return a + b
