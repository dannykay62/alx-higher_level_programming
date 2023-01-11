#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Returns number of lines of a text file
    Args:
    filename (str): Filename
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
