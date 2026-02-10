#!/usr/bin/python3
"""A module holding IO utilities,
This files holds append_write(filename, text)
"""


def append_write(filename="", text=""):
    """write_file - Writes to a file
    appending to anything,
    file is provided by name,
    text is a string
    """
    if filename == "":
        return

    written = 0
    with open(filename, mode='a', encoding="utf-8") as file:
        written = file.write(text)
    return written