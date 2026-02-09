#!/usr/bin/python3
"""A simple module
This modules holds a function that
reads and prints an entire file
"""


def read_file(filename=""):
    if filename == "":
        return

    with open(filename, 'r') as file:
        print(file.read())
