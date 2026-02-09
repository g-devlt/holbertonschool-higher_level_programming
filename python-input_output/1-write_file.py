#!/usr/bin/python3
"""A module holding IO utilities,
This files holds write_file(filename, text)
"""

def write_file(filename="", text=""):
    """write_file - Writes to a file
    overwrting everything,
    file is provided by name,
    text is a string
    """
    if filename == "":
        return

    written = 0
    with open(filename, mode='w', encoding="utf-8") as file:
        written = file.write(text)
    return written