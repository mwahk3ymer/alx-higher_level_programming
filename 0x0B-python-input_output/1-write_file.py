#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """
    Write a str to a text file (UTF8) and return the num of char.

    :param filename: The name of the text file to write to ().
    :param text: The string to be written to the file (g).
    :return: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
