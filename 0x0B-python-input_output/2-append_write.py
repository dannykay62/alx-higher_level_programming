#!/usr/bin/python3
"""This module a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends to the end of a file
    Args:
    filename (str): File to append
    text (str): text to append

    """
    with open(filename, 'a', encoding='utf-8'):
        return file.write(text)
