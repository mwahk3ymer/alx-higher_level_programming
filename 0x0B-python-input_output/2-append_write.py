#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def append_write(filename="", text=""):
    """
    Append a stri the number of characters added.

    :param filename: The name of the text file to append to
    :param text: The string to append to the file.
    :return: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
