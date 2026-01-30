#!/usr/bin/python3
"""A simple module for a basic Square class
"""


class Square:
    """A basic Square class
    """
    def __init__(self, size=0):
        """Initialization for Square instances.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


if __name__ == "__main__":
    square = Square(2)
    # square = Square(-2)
    print(type(square))
    print(square.__dict__)
