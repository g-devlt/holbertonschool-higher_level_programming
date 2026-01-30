#!/usr/bin/python3
"""A simple module for a basic Square class
"""


class Square:
    """A basic Square class
    """
    def __init__(self, sz):
        """Initialization for Square instances.
        """
        self.__size = sz


if __name__ == "__main__":
    square = Square(2)
    print(type(square))
    print(square.__dict__)
