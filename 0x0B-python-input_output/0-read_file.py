#!/usr/bin/python3
"""This module defines read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    Args:
    filename (str): Filename
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
