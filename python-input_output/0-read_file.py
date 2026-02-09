#!/usr/bin/python3
"""A simple module
This modules holds a function that
reads and prints an entire file
"""


def read_file(filename=""):
    """read_file - read files and
    prints them to the stdout
    """
    if filename == "":
        return

    with open(filename, mode='r', encoding="utf-8") as file:
        print(file.read())
