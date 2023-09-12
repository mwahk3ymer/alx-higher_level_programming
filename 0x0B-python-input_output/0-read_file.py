#!/usr/bin/python3

"""
Contains the read_file function
"""

def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    :param filename: The name of the text file toing).
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
